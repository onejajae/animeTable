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
* 요일별 애니 목록
    * 인자
        | Field | Type    | Description                           |
        | :---- | :-----: | ------------------------------------: |
        | day   | numeric | Min is 0 (Sunday). Max is 6(Saturday) |
        


애니편성표 두개 따로 보기 귀찮아서 만드는 프로그램

Java로 하려다가 할줄몰라서 간단하게 파이썬으로 만듬

객체지향 적용하고 싶었는데 머가리 터질것같아서 관둠
