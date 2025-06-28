from dotenv import load_dotenv
from scrapy import Request, Spider

from common.enums.domains import Domains
from common.enums.modes import Mode
from common.enums.objectives import Objectives
from common.enums.spider_settings import SpiderSettings, SystemSettings
from common.enums.strategies import Strategies


class MyBlogSpider(Spider):
    name = "my_blog"
    s_domain = Domains.TISTORY
    s_objective = Objectives.PRACTICE
    s_strategy = Strategies.CATEGORY

    custom_settings = {
        SystemSettings.DOMAIN: Domains.TISTORY,
        SystemSettings.OBJECTIVE: Objectives.PRACTICE,
        SystemSettings.STRATEGY: Strategies.CATEGORY,
        SystemSettings.MODE: Mode.LOCAL,
        SpiderSettings.DOWNLOAD_DELAY: 3,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        load_dotenv()

    async def start(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)
