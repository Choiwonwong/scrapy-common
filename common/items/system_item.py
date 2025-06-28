from dataclasses import dataclass


@dataclass
class SystemItem:
    _id: str = None  # domain_objective_strategy_execute_id_sequence
    _domain: str = None
    _objective: str = None
    _strategy: str = None
    _started_at: str = None  # Spider 시작 시간
    _execution_id: str = None  # spider 구분 값 based on s_started_at - %Y%m%d%H%M%S
    _collected_at: str = None  # 데이터 수집 시간
    _timezone: str = None  # TZ
