# airbnb-clone-backend

> ### #3.0 Run Server (04:57)

**서버 키는 법**
airbnb-clone-backend 폴더 위치 아래에서 `python manage.py runserver` 명령어를 터미널에서 실행해준다.

**서버 닫는 법**
`Ctrl + C`로 중지한다.

> ### #3.1 Migrations (07:16)

**admin page**
/admin/ 페이지로 가려함.

- /admin/ 페이지가 접속이 안되는 경우
  DB에 django_session 이라는 테이블이 없기 때문이다.

서버를 열면서 생긴 'db.sqlite3' 폴더는 DB파일인데 비어있다.

- migration 작업을 통해 문제 해결
  migration은 DB의 state를 수정하는 작업을 의미한다.
  ![Alt text](img/1.png)
  18개의 migration이 있다.

  `python manage.py migrate` 명령어를 터미널에 실행시켜 문제를 해결한다.
  ![Alt text](img/2.png)

- /admin/ 페이지 로그인 시 로그인 오류화면을 볼 수 있음

![Alt text](img/3.png)
