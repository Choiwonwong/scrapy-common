import logging
from copy import deepcopy

from scrapy.http import HtmlResponse

from common.items.my_blog.my_blog_item import MyBlogItem


class MyBlogHeaders:
    BASE = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ko-KR,ko;q=0.9",
        "priority": "u=0, i",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    }

    @classmethod
    def with_referer(cls, referer: str) -> dict:
        headers = cls.BASE
        headers["referer"] = referer
        return headers


class MyBlogUrls:
    HOME = "https://alive-wong.tistory.com/"

    @classmethod
    def get_paginated_url(cls, page_index: int) -> str:
        return f"{cls.HOME}?page={page_index}"


class MyBlogHtmlExtractor:
    @staticmethod
    def extract_last_page_index(response: HtmlResponse) -> int:
        pages = response.css("#paging > ul > li")
        pages_without_nextpage = pages.css("a.num")
        last_page_index = pages_without_nextpage[-1].css("span::text").get()
        return int(last_page_index)

    @staticmethod
    def extract_posts(response: HtmlResponse, base_item: MyBlogItem) -> list[MyBlogItem]:
        items: list[MyBlogItem] = []
        for post_info in response.css("#content div.index_wrap"):
            item = deepcopy(base_item)

            post_link_info = post_info.css("a.post_link")
            post_href = post_link_info.css("::attr(href)").get()
            item.post_id = post_href.replace("/", "")
            item.post_name = post_info.css("h2.post_title::text").get(default="").strip()
            item.post_content_summary = post_info.css("p.post_text::text").get(default="").strip()
            item.post_url = f"{MyBlogUrls.HOME}{item.post_id}"

            if post_info.css("div.thumnail>img::attr(src)").get():
                item.post_thumbnail = f"https:{post_info.css('div.thumnail>img::attr(src)').get()}"

            post_list_info = post_info.css("ul.post_list")
            item.post_category = post_list_info.css("span.post_category_name::text").get(default="").strip()
            item.post_date = post_list_info.css("li.post_date::text").get(default="").strip().replace("· ", "")
            post_comment = post_list_info.css("li.post_comment > span")
            if len(post_comment) == 2:
                item.post_comment_count = int(post_comment[-1].css("::text").get(default=0))
            else:
                logging.error(f"need to check : dueto post_comment - {item.page_url} - {item.post_url}")

            items.append(item)
        return items
