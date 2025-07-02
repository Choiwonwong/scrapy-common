# Goal
make crawling modules based on Scrapy(HTTP) for me or my stakeholders

### (Kor) 규칙 
#### 전반
1. (Must) spider에는 HTTP Call & Item 관리와 관련된 로직만 작성되어야한다.
2. (Must) 파싱 로직은 별도로 분리해서 작성하고, 메소드의 파라미터는 response 인스턴스만으로 제한한다.
3. (Must) 유틸 디렉토리에는 모든 스파이더에서 사용될 수 있는 기능만 작성해야한다. 각 도메인 별 유틸 함수는 spider와 같은 위치에 관리한다.
4. (Must) Item 클래스는 수집하는 변수만 선언해 완전하게 관리한다. 
5. (Should) 다음 콜백 함수에 전달하는 데이터를 전달하기 위해선 cb_kwargs을 사용하되, 하나의 인스턴스만 사용한다.
6. (Must) Call Flow는 User Flow를 모방한다.

#### Item Class
1. (Should) Call Depth 별로 1개의 Data Class를 관리하는 걸 권장한다.
2. (Must) next call에 사용되는 url, body 및 개별 파라미터들은 저장한다.
3. (Must) Result Schema에 관여하는 클래스는 1개여야한다.

### (Eng) Rules
#### Overall
1. (Must) Only logic related to HTTP Call & Item management should be written in the spider.
2. (Must) Parsing logic should be written separately and the parameters of methods should be limited to response instances only.
3. (Must) Only functions that can be used by all spiders should be written in the Util directory. Each domain-specific utility function is managed in the same place as the spider.
4. (Must) The Item class is completely managed by declaring only the variables it collects.
5. (Should) Use cb_kwargs to pass data to the following callback functions, but use only one instance.
6. (Must) Call Flow must impersonate User Flow.

#### Item Class
1. (Should) It is recommended to manage one Data Class per Call Depth.
2. (Must) Store the url, body, and individual parameters used for the next call.
3. (Must) Only one class should be involved in the Result Schema.

## Code Quality
this project uses [Ruff](https://github.com/astral-sh/ruff) for code formatting and linting.

```bash
# Install development dependencies
pip install ruff

# Format and check code
ruff format .
ruff check --fix .
```

## Pakaging
this project use [Pixi](https://pixi.sh/latest/)