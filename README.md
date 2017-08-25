# 애니편성표 통합 API

### 다음 두 API를 한번에 볼 수 있도록 해줍니다.
>   1. OHLI 애니편성표     : http://ohli.moe/api/
>   2. Anissia 애니편성표  : http://www.anissia.net/?m=1&b=4


### 현재 사용가능한 기능
>   1. Python 상에서 각각의 API 불러오기
>   2. 두 개의 API 병합하기
>       * 요일별 목록 
>       * 각각의 자막 제작자 목록


### 레퍼런스
>* 요일별 애니 목록
>    * Parameter
>
>       | Field |   Input type  |              Description              |
>       |:-----:|:-------------:|:-------------------------------------:|
>       | day   | numeric       | Min is 0(Sunday). Max is 6(Saturday). |
>
>   * Response
>
>       |     Field    |   Type   |             Description                 |
>       |:------------:|:--------:|:---------------------------------------:|
>       | anissia_code | numeric  | Anissia animation code                  |
>       | ohli_code    | numeric  | OHLI animation code                     |   
>       | s            | string   | Animation name                          |
>       | t            | HHmm     | Broadcasting air time                   |
>       | l            | string   | Animation official site url             |
>       | sd           | yyyyMMdd | Date when series started                |
>       | ed           | yyyyMMdd | Date when series would end              |
>       | a            | boolean  | Indicates if there is **not** a hiatus. |
>       *장르정보를 'string'으로 포함하는 필드가 'g' 이름으로 추가될 수 있음.*
>
>   * Errors
>
>
>* 애니별 자막 목록
>   * Parameters
>
>       |     Field    | Input type |       Description      |
>       |:------------:|:----------:|:----------------------:|
>       | anissia_code | numeric    | Anissia animation code |
>       | ohli_code    | numeric    | OHLI animation code    |
>
>   * Response
>
>       |  Field  |      Type      |                           Description                           |
>       |:-------:|:--------------:|:---------------------------------------------------------------:|
>       | s       | float          | Series number                                                   |
>       | d       | yyyyMMddHHmmss | Date-time when subtitle is uploaded                             |
>       | n       | string         | Subtitle publisher name                                         |
>       | a       | string         | Subtitle download link                                          |
>       | anissia | boolean        | Indicates if subtitle information was provided from Anissia api |
>       | ohli    | boolean        | Indicates if subtitle information was provided from OHLI api    |
>
>   * Errors
>
>






애니편성표 두개 따로 보기 귀찮아서 만드는 프로그램

Java로 하려다가 할줄몰라서 간단하게 파이썬으로 만듬

객체지향 적용하고 싶었는데 머가리 터질것같아서 관둠
