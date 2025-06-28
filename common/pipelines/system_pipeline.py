from copy import deepcopy
from multiprocessing import Value

from scrapy.crawler import Crawler

from common.enums.settings import SystemSettings
from common.items.system_item import SystemItem
from common.utils.datetime import CustomDateTime


class SystemPipeline:
    target_spider_class = None
    target_item_class = None

    id_counter = Value("i", -1)  # Thread-Safe

    def __init__(
        self,
        activated: bool,
        _domain: str,
        _objective: str,
        _strategy: str,
        _started_dt: str,
        _timezone: str,
        _execution_id: str,
        custom_date_time: CustomDateTime,
    ) -> None:
        self.activated = activated
        self._domain = _domain
        self._objective = _objective
        self._strategy = _strategy
        self._started_dt = _started_dt
        self._timezone = _timezone
        self._execution_id = _execution_id
        self.custom_date_time = custom_date_time

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        spider_instance_class = crawler.spider.__class__

        _domain = str(crawler.spider.custom_settings.get(SystemSettings.DOMAIN))
        _objective = str(crawler.spider.custom_settings.get(SystemSettings.OBJECTIVE))
        _strategy = str(crawler.spider.custom_settings.get(SystemSettings.STRATEGY))
        _tz = crawler.spider.custom_settings.get(SystemSettings.TZ, None)

        custom_date_time = CustomDateTime(tz=_tz)
        now = custom_date_time.now()
        _started_dt = custom_date_time.transform_started_at(now)
        _timezone = custom_date_time.get_tz(now)
        _execution_id = custom_date_time.transform_execution_id(now)

        return cls(
            activated=cls.target_spider_class == spider_instance_class,
            _domain=_domain,
            _objective=_objective,
            _strategy=_strategy,
            _started_dt=_started_dt,
            _timezone=_timezone,
            _execution_id=_execution_id,
            custom_date_time=custom_date_time,
        )

    def process_item(self, item, spider):
        if self.activated:
            return self._process_item(item)
        return item

    def _process_item(self, item) -> SystemItem:
        if isinstance(item, dict):
            for key_different_with_item_class in set(item.keys()) - set(self.target_item_class.__annotations__.keys()):
                del item[key_different_with_item_class]
            item: SystemItem = self.target_item_class(**item.copy())
        else:
            item: SystemItem = deepcopy(item)

        item._domain = self._domain
        item._objective = self._objective
        item._strategy = self._strategy
        item._started_at = self._started_dt
        item._timezone = self._timezone
        item._execution_id = self._execution_id

        item._collected_at = self.custom_date_time.get_collected_at()

        with self.id_counter.get_lock():
            self.id_counter.value += 1
            item._id = f"{self._domain}_{self._objective}_{self._strategy}_{self._execution_id}_{self.id_counter.value:09}"
        return item
