from copy import deepcopy

from dotenv import load_dotenv
from scrapy import Request, Spider
from scrapy.http import HtmlResponse

from common.enums.domains import Domains
from common.enums.modes import Mode
from common.enums.objectives import Objectives
from common.enums.settings import SpiderSettings, SystemSettings
from common.enums.strategies import Strategies
from common.enums.tz import TimeZone
from common.items.my_blog.my_blog_item import MyBlogItem
from common.spiders.my_blog.my_blog_utils import MyBlogHeaders, MyBlogHtmlExtractor, MyBlogUrls


class MyBlogSpider(Spider):
    name = "my_blog"

    custom_settings = {
        SystemSettings.DOMAIN: Domains.TISTORY,
        SystemSettings.OBJECTIVE: Objectives.PRACTICE,
        SystemSettings.STRATEGY: Strategies.CATEGORY,
        SystemSettings.MODE: Mode.LOCAL,
        SystemSettings.TZ: TimeZone.KST.value,
        SpiderSettings.DOWNLOAD_DELAY: 3,  # Just for practice
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        load_dotenv()

    async def start(self):
        yield Request(
            url=MyBlogUrls.HOME,
            headers=MyBlogHeaders.BASE,
            callback=self.prepare_pagination,
        )

    async def prepare_pagination(self, response: HtmlResponse):
        item: MyBlogItem = MyBlogItem()
        last_page_index: int = MyBlogHtmlExtractor.extract_last_page_index(response=response)

        for page_index in range(1, last_page_index + 1):
            item.page_index = page_index
            item.page_url = MyBlogUrls.get_paginated_url(page_index=page_index)
            yield Request(
                url=item.page_url,
                headers=MyBlogHeaders.BASE,
                callback=self.pase_pagination,
                cb_kwargs=dict(item=deepcopy(item)),
            )

    def pase_pagination(
        self,
        response: HtmlResponse,
        item: MyBlogItem,
    ):
        items: list[MyBlogItem] = MyBlogHtmlExtractor.extract_posts(response=response, base_item=item)
        for item in items:
            yield item
