import sys
from datetime import datetime

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run_spider(spider_name: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"output/{spider_name}/{timestamp}.csv"

    settings = get_project_settings()
    settings.set(
        "FEEDS",
        {
            output_file: {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": True,
            }
        },
    )

    process = CrawlerProcess(settings)
    process.crawl(spider_name)
    process.start()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python crawl.py <spider_name>")
        sys.exit(1)

    spider = sys.argv[1]
    run_spider(spider)
