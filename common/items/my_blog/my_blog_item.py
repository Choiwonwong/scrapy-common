from dataclasses import dataclass

from common.items.system_item import SystemItem


@dataclass
class MyBlogItem(SystemItem):
    page_index: int = None
    page_url: str = None

    post_id: str = None
    post_name: str = None
    post_content_summary: str = None
    post_url: str = None
    post_thumbnail: str = None
    post_category: str = None
    post_comment_count: int = None
    post_date: str = None
