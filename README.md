# iPark &nbsp;&nbsp;|&nbsp;&nbsp; 22년 7월 7일 - 22년 8월 16일 (1주)

### 서비스 소개 </br>

<details>
<summary>
서울시 공원들을 소개해주고 공원을 중심으로 지역 커뮤니티를 구성하는 서비스입니다.
</summary>
</br>

### 

서울시 공원들을 옵션과 지역구를 선택하거나 초성순으로 원하는 조건의 공원을 찾거나 검색하여 공원의 정보를 확인할 수 있습니다.

선택한 공원의 가까운 공영주차장을 거리순으로 추천을 받을 수 있으며, 공원 리뷰를 댓글로 달아 다른 사용자들과도 소통이 가능합니다.

사용자들은 공원을 중심으로 게시글을 작성하여 나눔마켓을 열거나 소통을 할 수 있습니다.

게시판은 커뮤니티와 나눔마켓으로 나누어져있으며 게시글 제목이나 내용을 검색할 수도 있고 댓글 작성하거나 삭제할 수도 있습니다.

서비스 특성상 모바일 접속자가 많을 걸로 예상하여 반응형을 적용하였습니다.

[🔗 팀 백엔드 리포](https://github.com/2JYK/iPark_django_backend)<br>
[🔗 팀 프론트엔드 리포](https://github.com/2JYK/iPark_frontend)<br>

</details>

서비스 사이트 >> https://www.ilovepark.net/


### 목차

[1. 개발환경](#개발환경) <br>
[2. 나의 역할](#나의-역할) <br>
[3. 사용자 피드백](#사용자-피드백) <br>
[4. 기능 명세서](#기능-명세서) <br>
[5. 데이터베이스 ERD](#데이터베이스-erd) <br>
[6. API 설계](#api-설계) <br>

<br>

## 개발환경
Backend : <img src="https://img.shields.io/badge/Python-3.9.10-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Django REST framework-092E20?style=flat-square&logo=Django REST framework&logoColor=white"/> 

Open API:
- SearchParkInfoService | Seoul OpenAPI
- NAVER Maps JavaScript API V3
- REST API | Kakao

Frontend : <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS&logoColor=white"/> <img src="https://img.shields.io/badge/jQuery-0769AD?style=flat-square&logo=jQuery&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=white"/> 

DataBase : <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=PostgreSQL&logoColor=white"/> 

Infra : <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/> <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/> <img src="https://img.shields.io/badge/Let's Encrypt-003A70?style=flat-square&logo=Let's Encrypt&logoColor=white"/> 
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=flat-square&logo=Amazon EC2&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=flat-square&logo=Amazon RDS&logoColor=white"/> 

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<br>

## 나의 역할

- 프로젝트 모델링
- 공공 데이터 csv파일 정제 후 JSON 파일로 변환하여 데이터 관리
- 공원 상세 정보 페이지 구현
    - 공원의 데이터를 serializer에 넣어 변환시키고 get 메소드를 사용하여 응답을 보냄
    - 백에서 받은 공원 상세 정보는 sessionStorage에 넣어 페이지가 로드됨과 동시에 보여짐
    - 공원의 조회수 기능 : 모델링 작업시 업데이트 수식을 작성하고 get 메소드가 실행됐을 때 실행
- 공원 댓글 기능 구현(http method별 설명)
    - get
        - serializer로 변환된 해당 공원의 댓글을 생성순서 순으로 보여줌
        - `count()`를 사용해 댓글의 총 갯수를 구하고, 댓글의 데이터와 함께 응답을 보냄
        - 한 페이지에는 10개의 댓글만이 보일 수 있도록 수식 작성
        - 토큰을 확인하여 사용자가 댓글 작성자일 경우에만 수정 버튼이 보이게 하는 프론트 작업 진행
    - post
        - if문을 작성으로 댓글을 작성하고자 하는 사용자가 익명인지 아닌지를 구분
        - `is_valid()` 를 사용하여 해당 필드의 형식에 맞는지 검증을 거친 후에 댓글 작성
    - put
        - if문을 작성으로 댓글을 작성하고자 하는 사용자가 익명인지 아닌지를 구분
        - try문 댓글과 사용자 예외 처리
        - 수정할 데이터들은 `partial=True` 을 사용해 부분 수정
        - `is_valid()` 를 사용하여 해당 필드의 형식에 맞는지 검증을 거친 후에 댓글 수정
    - delete
        - if문을 작성으로 댓글을 작성하고자 하는 사용자가 익명인지 아닌지를 구분
        - try문 댓글과 사용자 예외 처리 후 delete()함수를 사용해 댓글 삭제
- 카카오 소셜 로그인
    - OAuth 적용
    - try문을 사용하여 사용자 유무를 판단하여 에러 처리
        - status에 따른 프론트 작업
    - 사용자에 관한 데이터베이스가 있는지 없는지 이메일과 패스워드를 확인하는 if문 작성
- 배포 및 지속적인 업데이트 경험
    - 빌드 작업 : Docker
    - 백엔드 : AWS EC2
    - 데이터베이스 : AWS RDS PostgreSQL
    - 프론트엔드 : Netlify
    - nginx 컴파일 및 빌드 작업
- HTTPS 보안강화
    - letsencrypt 로 인증서 발급 진행
        - certbot SSL 적용
<br>

## 사용자 피드백

- 프로젝트의 방향이나 여건 상 맞지 않는 피드백은 필터링하고 7일의 기간동안 마무리할 수 있을 것 같은 피드백을 선별해 아래와 같이 해결
- 공원과 공영 주차장 공공 데이터들은 인터넷으로는 추가적으로 조사해 퀄리티를 높일 수 없다 판단해 보류

<img width="700" alt="185892052-7cecef17-bb12-4cf0-ab2a-f6d28a736bda" src="https://user-images.githubusercontent.com/104303285/189310257-5f66cb53-9416-4a4d-aa34-1c48739eeb8b.png">


<br>


<br>

## 기능 명세서
<details>
<summary> 메인페이지 </summary>
<pre>
- 상단바
    - 네비게이션을 통해 해당 페이지로 이동 또는 로그인/로그아웃을 할 수 있음
        - 공원 상세 페이지
        - 커뮤니티 페이지
        - 계정관리 페이지
        - 로그인/로그아웃
    - 토글
        - 공원 클릭시 공원 상세 내용 페이지로 이동
        - 기본값으로 가나다순으로 공원 정렬
    - 즐겨찾기
        - 관심있는 공원 목록을 확인할 수 있음
    - 내가 쓴 게시글
        - 커뮤니티에서 작성한 게시글들을 조회할 수 있음
- 공원 검색 버튼을 눌러 공원 검색 페이지로 이동해 원하는 조건의 공원을 찾을 수 있음
- 커뮤니티 버튼을 눌러 커뮤니티 페이지로 이동하여 게시글을 조회,작성할 수 있음
</pre>
</details>

<details>
<summary> 로그인 페이지 </summary>
<pre>
- 로그인
    - 카카오 계정 혹은 가입한 아이디로 로그인
    - 로그인에 성공하면 <span style="color: #FFA7A7;">access token, refresh token, payload</span>가  local Storage에 담김
        - payload의 exp를 통해 access token의 만료를 계산
        - 서비스를 이용하는 도중 access token이 만료되면 refresh token을 통해 갱신해주어 사용자가 서비스를 지속적으로 이용할 수 있도록 함
    - 카카오 로그인
        - 팝업을 통해 카카오 로그인을 진행함.
        - 필수 수집항목으로는 username, email 값을 받음
            - 카카오 계정에서의 <span style="color: #FFA7A7;">email, username</span> 값이 데이터베이스에 있을 경우
                - 비밀번호 값이 함께 존재한다면 자동로그인을 시켜주어 token, payload를 local Storage에 담아주고, 메인페이지로 이동
                - 비밀번호 값이 없다면 카카오계정에서 받은 <span style="color: #FFA7A7;">email, username, fullname</span> 값을 회원가입란으로 보내주어 추가적인 회원정보를 입력할 수 있도록 유도
            - 카카오 계정에서의 <span style="color: #FFA7A7;">email, usernameM</span> 값이 데이터베이스에 없을 경우 카카오 팝업을 띄어준 후 카카오 계정값을 받아 회원가입란으로 보내주어 추가적 회원정보를 입력할 수 있도록 유도
- 아이디 찾기
    - 회원가입을 할 때 입력한 정보인 <span style="color: #FFA7A7;">이메일, 핸드폰 번호</span> 확인을 통해 아이디를 찾을 수 있음
    - 가입한 내역이 있는 사용자라면 알림창을 띄어주어 본인의 아이디를 확인시켜줌
- 비밀번호 변경
    - 가입한 아이디와 이메일 확인을 통해 비밀번호를 변경할 수 있음
    - 새로운 비밀번호는 2 번 입력해 제대로 작성되었는지 확인
    - 영어 소문자/숫자/특수문자를 필수적으로 사용해야 하며 8 자리 이상의 형식을 맞춰야 함
- 기존에 가입한 사용자가 아니라면 회원가입 버튼을 눌러 회원가입 페이지로 이동할 수 있음
</pre>
</details>

<details>
<summary> 회원가입 페이지 </summary>
<pre>
- 회원가입
    - 카카오 계정 혹은 계정 생성으로 간편 가입
        - 카카오 로그인의 경우, 카카오에서 가져온 아이디, 이메일 등의 정보가 자동기입되어 있음
        - 기입되어 있는 정보들을 수정할 수 있으며, 나머지 값들도 입력해야 회원가입이 진행됨
    - 정해진 형식에 맞게 기입해야 회원가입 가능
        - 아이디 : 6 자리 이상
        - 이메일 : 이메일 형식에 맞게 작성 필요
            - <span style="color: #FFA7A7;">naver, google, kakao, daum, nate, outlook</span> 계정만 가입 가능
        - 비밀번호 : 영어 소문자/숫자/특수문자를 필수적으로 사용해야 하며 8 자리 이상
        - 핸드폰 번호 : <span style="color: #FFA7A7;">010-0000-0000</span> 의 형식으로 작성
- 회원가입이 완료되면 로그인 페이지로 이동
- 이미 계정이 있는데 해당 페이지에 들어온 경우 로그인 페이지로 돌아갈 수 있도록 버튼 생성
</pre>
</details>

<details>
<summary> 공원 검색 페이지 </summary>
<pre>
- 공원 옵션
    - 8 가지의 공원 특성
    - 서울시 25개 자치구
- 공원 옵션을 선택해 사용자가 원하는 조건의 공원을 검색할 수 있음
    - 3 가지의 방법으로 공원을 검색할 수 있음
        - 하나 또는 여러 개의 공원의 특성을 통해 검색 가능
        - 하나 또는 여러 개의 지역을 통해 검색 가능
        - 공원의 특성과 지역을 동시에 선택해 검색 가능
- 가로 스크롤을 이용해 검색된 공원 목록을 확인
- 조회수가 많은 순으로 공원을 사용자에게 제시함
    - 한 번도 조회가 되지 않은 공원은 제시되지 않음
</pre>
</details>

<details>
<summary> 공원 상세 내용 페이지 </summary>
<pre>
- 공원 상세 정보
    - 공원 이름, 주소, 사진, 시설, 설명, 전화번호, 홈페이지
    - 지도
        - 지도를 움직여 주변 시설들을 확인할 수 있음
        - 지도 내 마커 클릭시, 길찾기 기능을 이용한 공원으로 가는 경로 검색
- 즐겨찾기
    - 즐겨찾기 버튼을 눌러 즐겨찾기 페이지에서 모아볼 수 있음
    - 즐겨찾기 버튼을 다시 누르면 해제됨
- 댓글
    - 해당 공원에 대한 댓글을 이용해 사용자간의 소통이 가능함
    - pagination을 사용해 한 번에 보여주는 댓글의 개수는 10개
    - 댓글의 작성자는 본인의 댓글을 수정, 삭제를 할 수 있음
</pre>
</details>

<details>
<summary> 즐겨찾기 페이지 </summary>
<pre>
- 사용자가 즐겨찾기한 공원들을 최신순으로 정렬
- 삭제 버튼을 눌러 즐겨찾기한 공원을 삭제
- 공원의 이미지 혹은 이름을 클릭하여 공원의 상세 정보 페이지로 이동
</pre>
</details>

<details>
<summary> 커뮤니티 페이지 </summary>
<pre>
- 첫 페이지는 전체 게시글로, 모든 사용자들이 작성한 게시글을 보여줌
- 게시판 고르기, 공원고르기(드롭다운)를 클릭하여 해당 게시판을 확인할 수 있음
    - <span style="color: #FFA7A7;"> 커뮤니티 | 나눔마켓 | 내가 쓴 게시글 </span>
    - <span style="color: #FFA7A7"> 선호하는 공원 </span>
- <span style="color: #FFA7A7">업로드</span> 버튼을 클릭하여 게시글 업로드 페이지로 이동
- 글의 제목을 클릭하여 해당 게시글 상세페이지로 이동
- 검색창을 사용하여 게시글 제목, 내용을 포함한 검색결과를 확인할 수 있음
- pagination을 사용해 한 번에 보여주는 페이지의 개수는 13개
</pre>
</details>

<details>
<summary> 게시글 업로드 페이지 </summary>
<pre>
- 태그 [ 커뮤니티 or 나눔마켓 ]를 선택
- 사진 / 제목 / 내용 기입
    - 사진은 입력하지 않아도 무관
- 업로드 버튼을 누르면 등록 완료 알림이 뜨며 커뮤니티 첫 페이지로 이동
- 작성된 게시글은 <span style="color: #FFA7A7">내가 쓴 게시글</span>에서 확인 가능
</pre>
</details>

<details>
<summary> 게시글 상세페이지 </summary>
<pre>
- 게시글에 대한 내용을 확인
    - 게시글 태그, 제목, 내용, 작성자, 작성일자, 조회수, 댓글수
- 게시글의 작성자에게는 수정, 삭제 버튼이 보여 해당 기능을 사용할 수 있음
- 게시글 상세페이지로 이동시 조회수 +1
- 댓글
    - 사용자들은 해당 게시글에 대한 댓글을 통해 자유롭게 소통이 가능함
    - 최대 200자 제한
    - 댓글의 작성자는 본인의 댓글을 삭제를 할 수 있음
</pre>
</details>

<br>

## 데이터베이스 ERD
<details>
<summary> Click ! </summary>
&nbsp;&nbsp;
<pre>
<img width="1242" alt="ipark" src="https://user-images.githubusercontent.com/104303285/185301146-12508b43-dd0f-4bd1-afa1-5666f2fab8ea.png">
</pre>
</details>

<br>

## API 설계
<details>
<summary> Click ! </summary>
&nbsp;&nbsp;
<pre>
<img width="959" alt="스크린샷 2022-08-18 오후 1 13 48" src="https://user-images.githubusercontent.com/99387514/185292781-29cb132d-5042-4c6a-a6c9-97a42363df09.png">

<img width="946" alt="스크린샷 2022-08-18 오후 1 19 53" src="https://user-images.githubusercontent.com/99387514/185292957-a321a78f-35e2-415e-898a-319c8ec9ca49.png">

<img width="927" alt="스크린샷 2022-08-18 오후 1 20 09" src="https://user-images.githubusercontent.com/99387514/185292976-b68e1ae6-630c-4bcf-a510-47db46ccd59e.png">
</pre>
</details>
