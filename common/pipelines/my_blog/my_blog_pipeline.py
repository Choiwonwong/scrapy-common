from common.items.my_blog.my_blog_item import MyBlogItem
from common.pipelines.system_pipeline import SystemPipeline
from common.spiders.my_blog.my_blog_spider import MyBlogSpider


class MyBlogPipeline(SystemPipeline):
    target_item_class = MyBlogItem
    target_spider_class = MyBlogSpider
