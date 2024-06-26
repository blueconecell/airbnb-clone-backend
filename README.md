# airbnb-clone-backend

<details>
<summary> #3.0 Run Server (04:57)
</summary>

**서버 키는 법**

airbnb-clone-backend 폴더 위치 아래에서 터미널을 킨 후 `poetry shell`로 `django` 가상환경으로 들어가준다.
그 다음 `python manage.py runserver` 명령어를 터미널에서 실행해준다.

**서버 닫는 법**

`Ctrl + C`로 중지한다.

</details>

<details>
<summary>
#3.1 Migrations (07:16)
</summary>

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

</details>

<details>
<summary>
#3.2 Recap (04:57)
</summary>

**migration**

migration 파일에는 DB를 변화시킬 수 있는 python 코드가 들어있다.

이중에는 `auth-user`파일이 있을 것이다. 유저 저장 테이블이다.

</details>

<details>
<summary>
#3.3 Super User (07:24)
</summary>

**관리자 페이지**

터미널을 하나 더 열고 `django` 가상환경으로 들어가준 뒤 `python manage.py createsuperuser`를 실행한다.

비밀번호 설정 시 유효성 검사를 자동으로 해줌을 볼 수 있다.

![Alt text](img/4.png)

`/admin/`으로 들어가 설정한 아이디 비번을 입력하면 관리자 페이지를 볼 수 있다.

![Alt text](img/5.png)

관리자 페이지에서 본인 계정의 비밀번호 변경, 다른 유저의 비밀번호 변경, 유저생성, 그룹생성 등의 작업을 할 수 있다.

</details>

<details>
<summary>
#3.4 Framework vs Library (10:35)
</summary>

**라이브러리와 프레임워크의 차이 설명**

우리가 import를 통해 `라이브러리`를 호출한다.

`프레임워크`는 우리가 쓴 코드를 호출한다.

config폴더의 `setting.py` 파일의 내용을 수정함으로써 사용자의 코드에 맞춰 웹페이지의 내용이 바뀌는 것을 볼 수 있다.

![Alt text](img/6.png)

(프레임워크의 특징이다)

</details>

<details>
<summary>
#3.5 Apps (07:14)
</summary>

**장고의 프로젝트는 application들로 이루어져 있다**

Airbnb를 예시로 든다.

(`room`)숙소 정보와 (`user`)숙소 주인정보나 고객정보를 위한 로직을 같은 파일에 두지 않고 따로 둘 것이다.

`room`을 업로드하고 수정하고 삭제하는 등의 로직과 정보를 DB에 저장하고 변경사항을 적용해야한다.

`user`들이 소통하고 본인의 숙소페이지를 관리하고 본인의 예약정보를 관리하고, DB에 정보를 저장하고 변경사항을 적용해야한다.

</details>

<details>
<summary>
#4.0 Models (10:43)
</summary>

**장고의 프로젝트는 application들로 이루어져 있다**

django가상환경에서 다음 명령어를 터미널에 입력한다.
`python manage.py startapp 어플리케이션_이름`

'어플리케이션\_이름'에 해당하는 폴더가 만들어진다.

house 어플리케이션에 대한 데이터의 detail을 `models.py`에 작성한다.

파일을 수정하고 저장하여도 자동으로 서버가 재시작 되지 않는데 django가 아직 house 어플리케이션에 대해 모르기 때문이다.

config폴더의 `setting.py`파일에 `INSTALLED_APPS`에 우리가 만든 어플리케이션을 추가한다.
![Alt text](img/7.png)

`"houses.apps.HousesConfig"` 추가하기

</details>

<details>
<summary>
#4.1 Migrations (11:55)
</summary>

**Migrations**

django는 자동으로 admin 패널을 우리의 데이터로 생성해준다.

house폴더 아래에 있는 `admin.py`파일에 다음코드를 추가해준다.

```python
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
```

House라는 모델을 추가해주는 것을 볼 수 있다.

![Alt text](img/8.png)

하지만 눌러보면 table이 없다는 오류가 뜬다.

직접 migration을 함으로써 table을 만들어 줄 수 있다.

새로운 터미널을 열고 django가상환경상태에 진입한 후, `python manage.py makemigrations` 명령어를 입력한다.

![Alt text](img/9.png)

house 폴더 아래에 migration 폴더가 생겼고, 그 안에 '0001_initial.py'파일이 생겼다.

![Alt text](img/10.png)

변경된 데이터베이스를 적용하기 위해 `python manage.py migrate` 명령어를 입력해준다.

![Alt text](img/11.png)

그러면 이제 Houses를 눌렀을 때 migrate한 데이터베이스가 보인다.

![Alt text](img/12.png)

'ADD HOUSE' 버튼을 눌러 예전에 미리 설정해두었던 db자료형에 맞춰 내용을 추가할 수 있다.

![Alt text](img/13.png)

Houses에 내용물을 하나 추가하고 서버를 껐다키면 전에 추가했었던 내용이 살아있는 것을 확인할 수 있다.

![Alt text](img/14.png)

</details>

<details>
<summary>#4.2 Recap (10:49)</summary>

기존에 설치된 앱과 새로만들어 추가한 앱을 분리하여 따로 합쳐준다.

`INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS`

migration을 테스트해보기위해 house폴더 아래에 있는 `models.py`에서 'price'를 'price_per_night'로 바꾼 후 변경사항을 적용시키기 위해 migration을 해준다.

![Alt text](img/15.png)

migration폴더 아래에 새로운 파이썬 파일이 생기고 변경사항이 기록된다.

![Alt text](img/16.png)

변경사항을 `python manage.py makemigrations`로 등록해주고, `python manage.py migrate`로 적용해준다.

![Alt text](img/17.png)

적용된 모습이다.

</details>

<details>
<summary>#4.3 Admin (13:08)</summary>

**admin 패널 추가설정하기**

admin패널에 들어가면 Houses 클래스로부터 만들어진 항목의 이름이 'House object(1)' 로 보인다.

model.py에서 House클래스에 `__str__()` 메소드를 수정해줌으로써 우리가 원하는 형태로 보이게 할 수 있다.

```
    def __str__(self):
        return self.name
```

admin.py에서 `list_display=[]`에 데이터 속성이름을 적어주면 해당 속성들을 미리보기 가능하다.

```
    list_display = [
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    ]
```

`list_filter=[]`를 추가해주면 오른쪽에 필터목록을 볼 수 있다.

![Alt text](img/18.png)

```
    list_filter = [
        "price_per_night",
        "pets_allowed",
    ]
```

`    search_fields = ["address"]`이 코드를 추가 함으로써 주소를 기준으로 검색할 수 있는 검색창이 생긴다.

`"address_startwith"`를 집어넣으면 검색키워드로 시작하는 것만 뜨고, 그냥 `"address"`만 넣으면 키워드가 중간에 들어있어도 모두 검색된다.

</details>

<details>
<summary>#4.4 Documentation (13:33)</summary>

**Documentation**

[장고문서](https://docs.djangoproject.com/en/4.2/ref/models/fields/)

Documents를 통해 admin패널에서 도움말, 데이터 이름, 데이터 숨기기, 리스트상태에서 수정가능하게 하기 등등의 많은 기능을 적은 코드로 사용할 수 있다.

It's insane~

</details>

<details>
<summary>#5.0 Introduction (11:52)</summary>

**User Applications 환경설정\_0**

인터프리트 설정을 poetry환경으로 잡아준다.

그러면 django 임포트할때 밑에 경고물결줄이 안뜬다.

</details>

<details>
<summary>#5.1 Custom Model (13:53)</summary>

**User Applications 환경설정\_1**

[Documents Link](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)

`python manage.py startapp users`로 새로운 커스텀 유저를 만들어준다.

기존 유저의 모든 것을 상속받아야함.

1.  `AbstractUser`의 모든 것을 상속받은 `User`를 커스터마이징하고,

2.  커스터마이징한 `User`를 Django에게 사용하겠다고 인지시켜야한다.

    2-1. 링크에서 추가해야하는 코드를 `setting.py`에 추가한다.

    2-2. user application을 설치해야하므로 `CUSTOM_APPS`에 추가해준다.

    2-3. 커스텀 USER를 만들었는데 이미 옛날에 만들어둔 USER와 충돌을 일으키기 때문에 서버를 끄고 DB를 삭제해준다. "db.sqlite3"을 삭제한다. 서버 재실행해준다.

    2-4. 그리고 houses에 있는 migrations 파일도 지워준다.(0001\_.... 이렇게 생긴 파일들). (폴더와 `__init__.py` 파일은 살려둠)

    2-5. `python manage.py makemigrations`를 해준다.

    ![Alt text](img/19.png)

    2-6. `python manage.py migrate`로 새정보로 업데이트해주고, 동기화된다.

3.  user모델을 admin패널에 추가한다.

    3.1 users폴더에 admin.py에 내용을 추가해준다.

    3.2 다시 페이지를 리로드하면 로그인을 다시해야하는데, DB를 지웠기 때문에 세션이 종료된 것이고, user로 새로 생성해 줘야한다.

    따라서 `python manage.py createsuperuser`로 user계정을 새로 만들어준다.

![Alt text](img/20.png)

유저가 분리되어 보인다. 이전에는 Groups와 같이 있었다.

</details>

<details>
<summary>#5.2 Custom Fields (06:23)</summary>

**Custom User Model**

파이썬 코드에 있는 모델 구조와 DB구조를 서로 동기화 하기 위해 추가작업(기본값 넣어주기 등의 작업)을 해줘야 한다.

만약 'is_host'필드에 기본값을 지정해주지 않고 `python manage.py makemigrations`를 해주면 동기화를 위한 오류를 발생시킬 것이다.

![Alt text](img/21.png)

추가한 'is_host' 필드는 기본값없이 Nill 값으로 추가가 불가능하다는 오류이다.

옵션1. 일회성 기본값제공하기. 하지만 기존 행들의 이 열 값들이 모두 null값이 된다.

옵션2. 이 작업을 중지하고 models.py에서 기본값을 지정해준다.

2번을 선택하여 추가작업을 해줄 것이다.

</details>

<details>
<summary>#5.3 Defaults (11:04)</summary>

**Adding Default**

DB를 수정하여 기존에 있었던 필드가 사라지면 원래 있어야 할 것이 없어져서 오류가 발생한다.

default 값이 필요한 필드에 default값을 넣어주고 makemigrations를 해준다.

웹에서 유저를 클릭하여 들어가보자.

하지만 필드가 non-editable 상태여서 오류가 발생하는 것을 볼 수 있다.

다음 강의에서 해결한다.

</details>

<details>
<summary>#5.4 Custom Admin (08:34)</summary>

**Admin pages modify**

어드민 페이지를 수정하였다.

</details>
<details>
<summary>#5.5 Foreign Keys (13:16)</summary>

**유저 연동시키기(model연결시키기)**

ForeignKey를 사용하여 사용자를 연결한다.

만약 사용자가 지워지면 어떻게 처리할 것인지 정해주어야만 한다.

NULL로 처리해줄 수 있다. 하지만 그 유저가 만든 house가 주인이 없는 채로 남아있으면 안됨으로 house도 같이 delete해주기 위한 CASCADE를 쓴다. `on_delete=models.CASCADE`

그 다음 db.sqlite3과 migrations 폴더에 있는 파일들을 모두 지워준다.(`__init__.py` 빼고)

초기화 해주는 과정이다.

초기화가 되었기 때문에 makemigrations, migrate, createsuperuser를 다 해준다.(jeongyeon, 123)

웹페이지에 들어가서 house에 추가를 해주면 아래에 새로운 필드가 생긴 것을 확인할 수 있다.

![Alt text](img/23.png)

박스를 클릭하면 사용자를 선택해줄 수 있다. 초기여서 '-----'와 'jeongyeon' 2개만 있다.

house가 user의 ForeignKey를 가지고 있다고 알려주었기 때문에 models를 연결할 수 있었다.

PositiveIntegerField를 사용하게되면 단순히 숫자를 저장하기만 한다. 하지만 ForeignKey를 사용하면 Django에게 참조하고 싶은 model을 알려줌으로써 연결을 해준다.

</details>

<details>
<summary>#5.6 Super Mega Recap (16:07)</summary>

**관계형DB를 Django에서 다루기**

사용자를 예시로 user테이블과 house테이블을 연결하였다.

만약 user테이블에있는 user가 하나 사라진다면, 그 user와 연관된 house를 어떻게 처리할 것인지가 문제가 된다.

house를 같이 삭제시키는 방법과 house의 user정보를 null로 만들어버리는 방법 2가지가 있다.

extensions에서 sqlite viewer를 설치하면 django의 sqlite db를 시각화해서 볼 수 있다.

다음에 model들을 생성할 것이기 때문에 house폴더를 삭제시켰다. 그리고 setting.py에서 custom_apps에 있는 house도 지워준다.

그다음 migration폴더에 있는 것도 지워서 초기화 해준다.

</details>
<details>
<summary>#6.0 User Model (11:38)</summary>

**최종 프로젝트에서 사용할 model만들기**

user 모델을 확장하였음

</details>
<details>
<summary>#6.1 Room Model (07:08)</summary>

**최종 프로젝트에서 사용할 model만들기**

rooms 모델을 새로 만들어줌

콘솔창에 `python manage.py startapp rooms`를 쳐서 새 모델을 만들어 주고, Config폴더에 있는 settings.py에 CUTSTOM_APPS에 `"rooms.apps.RoomsConfig",` 을 추가한다.

many-to-many 것들을 위해 나머지는 다음강의에

</details>
<details>
<summary>#6.2 Many to Many (13:19)</summary>

**최종 프로젝트에서 사용할 model만들기**

many to many 의 의미를 알기 위해서는 Many to one, One to many의 의미를 알아야 한다.

- room1, room2, room3 -> user1 (Many to one)

- user1 -> room1, room2, room3 (One to many)

Amenty model이 many to many relationship을 가진다.

Amenity1, Amenity2, Amenity3 => room1, room2, room3

그리고 반복을 피하기 위해서 생성된 날짜, 변경수정된 날짜를 저장하는 필드를 하나 만들어준다.

여기서 `auto_now_add=True`를 해주게 되는데 처음 생성되었을 때 날짜를 넣어주는 기능이다.

update는 `auto_now=True`를 넣어줘서 저장될 때마다 시간이 기록되게 한다.

근데 여기서 만들고 있는 시간 저장기능은 다른곳에서도 똑같이 사용될 것이다. 그러면 반복적으로 같은 코드를 사용해줘야하는데 이 중복되는 것을 막기 위해서 새로운 application을 만들어줄 것이다.

콘솔에 `python manage.py startapp common`으로 공통 코드를 위한 새 application을 만들어준다.

이 새로 만들어준 common모델에는 추상모델을 만들어준다. 이 모델은 db에 추가하지 않고 다른 모델에서 재사용하기 위한 모델이다. 이것은 blueprint같은 모델이다.

만들어준 common 모델에 아래부분에

```(python)
class Meta:
    abstract = True
```

을 적어준다면 django는 이 모델에 대해서 쓸모없는 db를 만들어내지 않는다.

사용하기 위해서는 사용하고자 하는 모델에 임포트를 먼저 한 후 `from common.models import CommonModel` 시작할 때 modles.Model부분을 `CommonModel` 로 바꿔적어주면 된다.

</details>
<details>
<summary>#6.3 Recap (08:00)</summary>

**최종 프로젝트에서 사용할 model만들기**

만든 rooms와 amenities를 웹상에서 확인해봄.

db에서 직접 확인해보면 생성날짜 수정날짜도 확인할 수 있다.

</details>
<details>
<summary>#6.4 Rooms Admin (12:49)</summary>

**최종 프로젝트에서 사용할 model만들기**

room과 amenity의 이름 수정

그리고 Amenity모델을 자동으로 복수형으로 표시하는 django의 기능 중 Amenitys라고 잘못된 복수형을 다음 코드로 바로잡아준다.

```(python)
class Meta:
    verbose_name_plural = "Amenities"
```

admin.py에서 목록에서 어떻게 보일지, 어떤 필터 적용기준으로 보여줄지 패널에서 시각화 할 수 있다.

</details>
<details>
<summary>#6.5 Experiences (12:27)</summary>

**최종 프로젝트에서 사용할 model만들기**
experience창 만들기

</details>

<details>
<summary>#6.6 Categories (11:02)</summary>

**최종 프로젝트에서 사용할 model만들기**
category 연결 만들기

</details>
<details>
<summary>#6.7 Reviews (08:28)</summary>

**최종 프로젝트에서 사용할 model만들기**
review 테이블만들기

</details>
<details>
<summary>#6.8 Wishlists (05:45)</summary>

**최종 프로젝트에서 사용할 model만들기**
wishlist 만들기

</details>

<details>
<summary>#6.9 Bookings (14:42)</summary>

**최종 프로젝트에서 사용할 model만들기**
booking 만들기

-> rooms, experiences 2개 모두 예약할 수 있는 booking기능을 만들 것이다. 2개중 선택을 할 수 있도록 choice클래스를 하나 만들어준다.

booking에서 check_in, check_out을 만들어 줄 때에는 DB에 시간을 포함하여 저장할 것인지 날짜만 저장할 것인지를 우리가 정하여 만들어줘야 한다.(여기서는 날짜만 저장하기로 함)

</details>
<details>
<summary>#6.10 Medias (10:11)</summary>

**최종 프로젝트에서 사용할 model만들기**
Media 만들기

OneToOneField를 만들었는데 고유한 것을 연결할 때 사용하였다.(드물게 사용함)

</details>

<details>
<summary>#6.11 Direct Messages (15:21)</summary>

**최종 프로젝트에서 사용할 model만들기**
direct_messages 만들기

dms로 이름지어도 되어서 그렇게 했음

application이름은 해당 모델의 폴더 아래에 app.py에서 name을 수정함으로서 바꿀 수 있다.

admin패널에서 추가적으로 문자 개수, 채팅방에 참여하고있는 사람수, 개시한 방에 평점 등의 추가적인 속성을 넣어줄 수 있을 것이다.

</details>
<details>
<summary>#7.0 Introduction (10:58)</summary>

**Django의 ORM**

콘솔창에서 shell로 db와 소통할 것이다.

`python manage.py shell`

models를 통해 db에 접근한다.

db에 있는 모든 room찾기

`from rooms.models import room`

`Room.objects.all()`

어떠한 속성으로도 찾을 수 있다.

`Room.objects.get(name="서울집")`

.get 뿐만아니라 .create, .filter도 있다

`room = Room.objects.get(name="서울집")`

처럼 변수에 저장하고

`room.created_at`,`room.name`,`room.id`등의 명령어를 입력할 수 있다.

`room.price = 2000`으로 하고 `room.save()`를 하게되면 db가 업데이트된다. 심지어 updated_at에 시간이 반영된다. 하지만 국제표준시간 기준이여서 9시간 느리게 보인다.

</details>

<details>
<summary>#7.1 filter, get, create, delete (14:10)</summary>

**ORM 용어들**

- `.get()` 특정한 object 하나만 찾고 싶을때

  `Room.objects.get(pk=1)` primary key 1로 찾을때

- `.filter()` 필터적용하여 가져오기

  - `Room.objects.filter(pet_friendly=True)`
    'pet_friendly'를 필터적용하여 가져오면 결과값 개수가 1개 이상이므로(0개가 나올 수 있음) `.filter()`를 사용해야한다. 만약 `.get()`을 사용하면 오류가 날 것이다.

  - filter는 유용하다. '속성'+ '\_\_필터값' 형식으로 underscore를 이용한다.

  - 부등호도 사용하다.

  `Room.objects.filter(price__gt=15)`

  - 검색어도 사용가능하다('seoul'이 들어간 방만 찾기 같은 행위)

    `Room.objects.filter(name__contains="서울")`

    `Room.objects.filter(name__startswith="서울")`

- `.all()` 모든것을 보여줌

- `.create()` db내용물 생성하기

  괄호안에 속성값을 잘 넣어줘야한다.

  `Amenity.objects.create(name="Amenity from the Console",  description="cool")`

- `.delete()` 선택한 db값을 삭제할 수 있다.

  `.get()`으로 삭제하고싶은 것을 고르고 삭제해준다.
  `Amenity.objects.get(pk=4).delete()`

      </details>

  <details>
  <summary>#7.2 QuerySets (07:01)</summary>

**QuerySets은 무엇인가**

연산자를 함께 묶어주는 역할을 한다.

filter 사용시 여러 속성을 ','로 묶어줄 수 있다.

db와 소통하지 않고 db에 있는 모든 데이터를 몽땅 꺼내온다.

QuerySet은 구체적으로 요청받을 때만 데이터를 제공할 것이다.

명령을 즉시 실행시켜주지 않고 데이터를 요청할 때만 제공한다.

1. 게으르기 때문에 db를 힘들게 하지 않는다.

2. 서로다른 QuerySet들을 연결할 수 있다.

all같은 db를 힘들게 할 수 있는 명령어를 실행한다면 db를 바로 다 보여주지 않고 QuerySet형태로 짧게 보여준다.

</details>

<details>
<summary>#7.3 Admin Methods (14:34)</summary>

**lookup 무엇인가**

"\_\_"연산자는 lookup연산자라고 부른다.

[Documentation link](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups)

QuerySet을 반환하는 메소드도 있고, 반환하지 않는 메소드도 있다.

새로운 db 콘솔 지식을 통하여 admin 패널에서 더 많은 것을 할 수 있다.

예를들면 .count()메소드를 통해 얼마나 많은 요소들이 있는지를 표시해줄 수 있다.

`"total_amenities",`이 항목을 rooms의 admin.py에 추가할 것이다. 하지만 이것은 미리 만들어주지 않았기 때문에 오류가 발생한다.(Room클래스의 메소드로 찾아내려 한다.)

2가지 방법이 있다.

1. 직접 model에 메소드를 추가하기. ORM을 이용하는 방법이다.

2. admin.py에 직접 메소드를 만들어주기. 메소드는 self뿐만 아니라 room도 매개변수로 갖게된다.

1번방법은 room에 항상 total_amenities메소드가 따라다닐 것이다. room을 쓸때마다 total_amenities도 필요하다면 1번방법이 좋다. 2번방법은 관리자 패널에서만 확인할 수 있다. 다른곳에서는 전혀 필요없고, 관리자 패널에만 필요하다면 2번방법이 좋을 수 있다.

```
#(admin.py)
def total_amenities(self, room):
    return room.amenities.count()
```

```
def total_amenities(self):
    return self.amenities.count()
```

이렇게 해줌으로서 count()메소드로 amenities개수를 표현해줄 수 있다.

</details>
<details>
<summary>#7.4 ForeignKey Filter (11:33)</summary>

**foreignKey로 필터링하기**

reverse accessors : 관계를 뒤집어서 접근하도록 하는 것.

사용하는 이용 : 반대방향으로 원하는 정보를 찾을 때

room 모델은 user모델을 foreignKey로 포인팅하고 있다.

reverse란 user를 가리키고 있는 model을 찾기 위한 것. 반대방향으로 원하는 것을 찾아가는 것.

예를 들어 room.owner은 room에서 user를 찾아내는 것이다. 근데 user에서 room을 찾아내는 방법, 이것이 reverse이다.

`Room.objects.filter(owner__username="jeongyeon")`

이런식으로 작성하면 해당 유저의 모든 room을 QuerySet으로 보여준다.

`Room.objects.filter(owner__username__startswith="j")`

이런것도 가능하다(~로 시작하는 것 찾기 필터)

이런 기능이 반복적으로 많이 필요한 경우가 있다. 예를들어 인스타그램에서 creater가 사진을 올리는 기능이 있고 그 creater를 클릭하여 그사람이 올린 사진들을 보는 행위 reverse가 있는데 둘다 반복적으로 많이 쓰이는 기능이 될 것이다.

room.owner.username은 가능하다. 방을 업로드한 유저의 이름을 보는 기능이다. 하지만 반대로 유저의 이름을 기준으로 그 유저가 올린 방을 모두 찾아보는 기능 user.rooms 이러한 기능은 만든적이 없다. reverse로 찾아야 하는 것이다. 하지만 코드를 손봐서 기능을 만들어 줄 수 있다.

</details>
<details>
<summary>#7.5 Reverse Accessors (11:27)</summary>

**Reverse Accessors**

콘솔에서 User를 임포트해와서 pk=1을 me라는 변수에 저장하자.

`dir(me)`를 통해 많은 메소드와 속성을 볼 수 있다.

`~_set`이라는 것이 많다. 이것이 reverse accessors이다.

`me.room_set.all()`을 입력하면 해당 유저의 모든 room을 보여준다.

새로운 유저를 만들어주자. (admin, adminpw1234) 방하나를 admin의 방으로 바꿔준다.

다시 명령어를 입력하면 방이 하나 없어져있다.

규칙 : ForeignKey는 매번 `_set`속성을 받는다.

review에서도 user와 연결시 ForeignKey를 사용했다. 따라서 `me.review_set`이 가능하다.

</details>
<details>
<summary>#7.6 related_name (07:47)</summary>

**Reverse Accessors 이름 커스터마이징**

A가 B에 대한 ForeignKey를 만들었다면 B는 A_set을 갖는다.

`user.room_set()`을 더이상 하지않고 `user.rooms`을 하도록 만들려면 rooms의 models.py에서 Room 클래스의 owner설정에서 `related_name="rooms",`을 추가하면 된다.

추가후 makemigrations, migrate을 해줘야 적용이 된다.(ORM shell콘솔도 껐다 켜준다.)

ForeignKey뿐만 아니라 ManyToMany도 바꿔줄 수 있다. 바꿀 수 있는건 모두 바꿔준다.

</details>

<details>
<summary>#7.7 Recap (06:33)</summary>

**Reverse Accessors 복습**

이미 만들어 놓은 속성이나 메소드를 반대방향으로 호출하고 싶을 때 추가적으로 만들지 않고도 사용가능한 기능.

related_name으로 이름을 바꿔줄 수 있다.

</details>
<details>
<summary>#8.0 Methods (13:42)</summary>

**리뷰 평균내서 보여주기**

일단 room에서 review를 볼 수 있게 메소드를 하나 만든다. 프론트에서 보여줄 목적도 있다.

```
def rating(room):
    return room.reviews.count()
```

이런식으로 ORM문법을 이용해 return값을 만들어준다.

```
for review in room.reviews.all().values("rating"):
```

for문으로 필요한 모든 리뷰를 불러올때 그냥 `.all()`을 해버리면 db가 고생을 한다. 따라서 뒤에 `.values("rating")`을 붙여서 필요한 값만 가져오도록 최적화를 해준 것이다.

</details>
<details>
<summary>#8.1 Search Fields (07:41)</summary>

**검색 필드**

room의 admin.py에 
```
search_fields = ("name", "price",)
```
를 추가하게되면 admin패널의 room에서 검색필드가 생성된다.

그리고 방의 이름이나 가격으로 방을 검색해볼 수 있다.

이러면 기본적으로 검색한 내용이 우리가 선택한 항목에 있는지 확인한다.

startswith 키워드는 앞에 `^`를 넣어주면 사용할 수 있다. (~로 시작하는 것 검색하기)

```
search_fields = ("^name", "^price",)
```

완전히 똑같은 것을 찾아주고 싶을 때는 `=`를 앞에 넣어주면 된다.

```
search_fields = ("=name", "=price",)
```

만약 사용자 이름으로 찾고 싶다면

```
search_fields = ("owner__username",)
```

이처럼 장고가 기본으로 제공하는 기능을 사용하여 만들어줄 수 있다.

Foreign Key를 이용하여 검색하는 방식이다. owner는 room model의 한 요소로 user로부터 관계되는 값이다.

</details>

<details>
<summary>#8.2 Admin Actions (09:18)</summary>

room을 삭제하려하면 장고는 연결된 관계같은 것들이 같이 삭제되거나 변경되는지 한눈에 보여주는 페이지를 띄워준다.

**admin action 추가하기**

admin action은 3개의 파라미터로 구성된다. 

1. 액션을 호출하는 클래스 
2. request객체
3. queryset 선택한 모든 객체를 반환
```
@admin.action(description="Set all prices to zero")
def reset_prices(modle_admin, request, queryset):
    print(modle_admin)
    print(dir(request))
    print(queryset)
```

위와 같이 체크박스에 선택한 room들을 queryset을 출력하여 확인해 볼 수 있다.

우리가 만들려는 기능은 선택한 방들의 가격을 0으로 바꾸는 것이다.

```
def reset_prices(modle_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()
```
</details>
<details>
<summary>#8.3 Custom Filters (16:19)</summary>


**나만의 필터 만들기**

admin.py에 클래스 내부에 `list_filter=(rating)`처럼 만들면 해당 필드명으로 필터를 만들 수 있었다.

관계, Foreign Key로도 필터를 만들 수 있다. User로 만들어보자

```
    list_filter = (
        "rating",
        "user__is_host",
        "room__amenities",
        "room__pet_friendly",
    )
```

이런식으로 Foreign Key로 관계를 통해 필터를 만들어 줄 수 있다.

Foreign Key의 또 다른 Foreign Key로도 필터를 만들어줄 수 있다.

리뷰에서 특정 단어를 포함하는 것만 보여주도록 필터를 만들어볼 수도 있다.

```
# SimpleListFilter를 상속받는다.
class WordFilter(admin.SimpleListFilter):
    # 필수 - 필터제목
    title="Filter by words!"
    # 필수 - URL에 뜨는 내용 'potato=어쩌구' 이렇게 URl에 나옴
    parameter_name="potato"
    # 필수 - 필터 내용이 어떤 것이 나와야하는지 Override되야하는 lookup method
    # 튜플 리스트를 반환해야한다.
    def lookups(self, request, model_admin):
        # 두번째 튜플요소를 화면에 보여준다.
        return [
            ("good", "Good"),
            ("oh", "Oh"),
            ("wow","Wow")
        ]
    # 필터를 거친 결과물을 보여주는 메소드
    def queryset(self, request, reviews):
        # request에 GET을 사용할 것이다.
        # 바뀐 url을 읽어서 값을 뽑아올 수도 있지만 self를 이용하여 값을 가져올 수 있다.
        word = self.value()
        if word:
            # 리뷰 내용물에 word와 같은 값을 뽑아준다.
            return reviews.filter(payload__contains = word)
        else:
            return reviews
```

이런식으로 직접 구현하여 단어가 들어있는지 여부로 필터를 만들어줄 수 있다.

여기서 3점미만은 bad, 3점 이상은 good 리뷰인 것으로 판단해주는 필터를 만들어보자.

```
# 3점미만은 bad, 3점 이상은 good로 나눠주는 필터
class good_or_bad(admin.SimpleListFilter):
    title = "3점미만 = bad, 3점이상 = good"
    parameter_name = "good_or_bad"
    def lookups(self, request, model_admin):
        return [
            ("good","good"),
            ("bad","bad"),
        ]
    def queryset(self, request, reviews):
        feel = self.value()
        if feel == 'good':
            return reviews.filter(rating__gte = 3)
        elif feel == 'bad':
            return reviews.filter(rating__lt = 3)
        else:
            return reviews
            
```

</details>
<details>
<summary>#8.4 Recap (04:45)</summary>


**Recap**

검색창 필드 `search_fields`, 사용자 액션 `@admin.action`, 사용자 지정 필터 3가지를 만들어 보았다.

</details>
<details>
<summary>#9.0 Views (09:18)</summary>


**Views**

config 폴더의 urls.py파일에서 url로 접속하면 어떻게 어디로 보낼지를 정해줄 수 있다.

view는 유저가 특정 url에 접근했을 때 작동하게되는 함수이다. 만들어 놓은 rooms, houses 등에 views.py가 하나씩 다있다.

views.py를 url에 import해올 것이기 때문에 굳이 views라는 이름을 갖을 필요는 없다. 다른 이름으로 해도 된다.

```
# rooms > views.py
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("hi")
```

기본적으로 view에서 함수를 만들면 request를 파라미터로 만들어줘야한다.
장고에서 기본적으로 제공하는 파라미터이기 때문이다. 

```
# url.py
from django.contrib import admin
from django.urls import path
from rooms.views import say_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms', say_hello)
]
```

이렇게 코드를 짠 후 `http://127.0.0.1:8000/rooms`로 접속하면 return 값인 hi가 출력된 것을 볼 수 있다.


</details>
<details>
<summary>#9.1 Include (06:04)</summary>


**URL들을 개별 파일로 만들 것이다.**

rooms의 url을 분리된 파일로 바꿀 것이다.

각 application의 url파일에 각 url들을 분리시켜줄 것이고 config로 묶어줄 것이다.

urls.py에 include를 임포트 해온 뒤, 우리가 원하는 url 주소로 이동할 때 include를 통해 각 어플리케이션의 url파일로 이동하게 할 것이다.

`path('rooms/', include("rooms.urls"))`

```
from django.urls import path
from . import views

urlpatterns = [
    path("",views.say_hello),
]
```

include를 통해 넘어가면 위처럼 세부 경로에 따라 어떤 화면을 view해줄지 정해줄 수 있게 된다. 지금은 room/ 까지만 만들어 둔 형태이다.

</details>
<details>
<summary>#9.2 URL Arguments (07:12)</summary>


**URL의 변수를 참조하자**

`path("<int:room_id>",views.see_one_room)`

꺽쇠 안에 `변수 자료형:변수명` 형식으로 써주면 url의 값을 변수로 사용할 수 있다. 여기서 int 자료형을 사용하였기 때문에 문자열을 url 뒤에 써주게 되면 오류를 자동으로 저료형 검사를 하여 띄워준다.

사용하는 url `views.see_one_room` 함수에는 변수를 매개변수로 받아줘야한다.

```
def see_one_room(request,room_id):
    return HttpResponse(f"see room with id: {room_id}")
```

</details>

<details>
<summary>#9.3 render (05:19)</summary>


**랜더링하기**

`render` 의 첫번째 매개변수는 request, 두번째 매개변수는 템플릿 이름이 들어온다. 세번째는 데이터를 넘겨줄 것을 넣어준다.

```
def see_all_rooms(request):
    rooms = Room.objects.all()
    return render(request, "all_rooms.html",{"rooms":rooms, 'title':'hello! this title comes from django!'} )
```

그리고 템플릿 폴더를 만들어 두고 그 안에 명시한 html파일을 만들어 내용을 적어준다. 세번째 매개변수로 넘겨받은 데이터를 사용하고자 하면 플라스크처럼 `{{}}`를 사용해준다

`<h1>{{title}}</h1>`

</details>

<details>
<summary>#9.4 Django Templates (06:42)</summary>


**템플릿에서 각 방 표시하기**

플라스크와 같은 문법을 사용해준다.

```
<h1>{{title}}</h1>

<ul>
{% for room in rooms %}
<li><a href="/rooms/{{room.pk}}">
    {{room.name}}</br>
    {%for amenity in room.amenities.all %}
    <span>- {{amenity.name}} </br> </span>
    {%endfor%}</a>
</li>
{%endfor%}
</ul>
```
`a` 태그를 사용하여 해당 방의 primary key를 링크로 걸어 방으로 넘어가게 만들어 주었다.

</details>

<details>
<summary>#9.5 DoesNotExist (08:54)</summary>


**한개의 방을 보기 위한 코드 작성하기**

```
def see_one_room(request,room_pk):
    room = Room.objects.get(pk=room_pk)
    return render(request, "room_detail.html",{'room':room,})
```

ORM을 활용하여 room의 세부 정보들을 가져와 room이라는 변수로 html파일로 넘겨준다.

```
<h1>{{room.name}}</h1>
<h3>{{room.country}}/{{room.city}}</h3>
<h4>{{room.price}}</h4>
<p>{{room.description}}</p>
<h5>{{room.category.name}}</h5>
```

room의 detail들을 메서드 형태로 가져오고, foreign키로 묶여있는 카테고리도 `room.category.name` 이런식으로 쉽게 가져올 수 있다.

**try except 로 예외처리하기**

만약 room_pk값으로 존재하지 않는 방의 정보를 요구할 때는 `404 not found`를 띄워 존재하지 않는 방이라고 알려야 한다.

try except문으로 예외처리를 해주고 프론트에서도 처리를 해준다.

```
def see_one_room(request,room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(request, "room_detail.html",{'room':room,})
    except Room.DoesNotExist:
        return render(request, "room_detail.html",{'not_found':True,})
```

만약 존재하지 않는 방이라면 `not_found`라는 변수에 `True`를 담아 보낸다.

```
{% if not not_found %}

    <h1>{{room.name}}</h1>
    <h3>{{room.country}}/{{room.city}}</h3>
    <h4>{{room.price}}</h4>
    <p>{{room.description}}</p>
    <h5>{{room.category.name}}</h5>
{% else %}
    <h1>404 Not Found 🤣</h1>
{% endif %}
```

프론트에서는 `not_found`변수의 부울값에 따라 렌더링을 다르게 해주면 된다.

</details>

<details>
<summary>#9.6 Django vs React (06:38)</summary>

**장고의 템플릿 vs 리액트**

장고 템플릿으로도 충분히 동적으로 만들 수 있지만 충분하지 않기 때문에 리액트를 사용할 것이다.

장고는 어드맨 패널과 ORM, JSON 전송에 사용할 것이고 화면구성(UI)에는 리액트를 사용할 것이다.

장고는 좋은 API서버이다. REST API는 장고의 REST framework이다.

</details>

<details>
<summary>#10.0 Rest Framework - Introduction (06:15)</summary>

**장고 rest 프레임워크**

오래되고 안정적인 프레임워크이고 장고를 사용하는 대부분의 회사의 표준이다.

`poetry add djangorestframework`

pip 말고 poetry를 통해 설치해줄 것이다. poetry 가상환경이 켜져있는 상태에서 설치해야한다.

설치 후 config폴더의 setting.py파일에 추가된 내용을 적어줘야한다.

`THIRD_PARTY_APPS = ['rest_framework',]`

`INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS`

설치된 rest framework를 사용할 수 있게된다.

</details>
<details>
<summary>#10.1 JsonResponse (12:39)</summary>

**Json으로 응답 넣기**

react를 사용하고 장고의 템플릿 기능을 사용하지 않기로 하였으니 render는 지운다.

```
from django.http import JsonResponse
from .models import Category

def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            'ok':True,
            'categories':all_categories,
            
        })
```

json을 웹페이지로 보낼 수 있는데 여기서 python객체를 json에 담아서 보내려면 serializable하지 않아서 오류가 뜨게 된다. 이 파이썬 객체를 json이 해독가능하게 바꿔줘야만 한다.

</details>

<details>
<summary>#10.2 api_view (06:56)</summary>

**파이썬 객체 json으로 바꿔주기**

```
from django.http import JsonResponse
from django.core import serializers
from .models import Category

def categories(request):
    all_categories = Category.objects.all()
    return JsonResponse(
        {
            'ok':True,
            'categories':serializers.serialize("json",all_categories),
            
        })
```

이렇게 번역해주는 serialize를 사용하면 json으로 바뀌어 잘 나오게 된다.

django serialization 프레임워크는 많은 기능을 제공하고 있지 않기 때문에 django rest 프레임워크를 사용할 것이다.

데코레이터를 이용한다. (`@admin.register~~~`)

```
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category

@api_view()
def categories(request):
    return Response(
        {'ok':True,
        }
    )
```

`rest_framework`의 데코레이터의 `api_view`와 `Response`를 이용하면 rest framework 특유의 렌더링 방법으로 json을 보여준다. 하지만 아직 serialize되지 않았다.

</details>
<details>
<summary>#10.3 Serializer (10:53)</summary>

**Serialize 파이썬 객체 JSON으로 번역해주기**

```
from rest_framework import serializers

class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField() 
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
```
직접 serializer를 구현해주었다.

```
from categories.serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category

@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories,many=True)
    return Response(
        {'ok':True,
        'categories': serializer.data,
        }
    )
```

구현한 serializer를 가져와 사용해줄 때, `many=true`를 해줘야 인자로 받은 파이썬 객체의 내용을 모두 받아드린다. 받아드린 파이썬 객체의 요소들을 보고 구현해 놓은 것만 번역하여 보여준다.

</details>

<details>
<summary>poetry 가상환경으로 파이썬 인터프리터 설정하기</summary>

1. 가상환경에서 `poetry env info`로 가상환경의 python.exe 파일의 주소를 알아낸다.

2. `Ctrl + Shift + P`로 파이썬 인터프리터를 설정해준다. 설정해줄때 1번에서 알아낸 주소를 복붙해주면 된다.

-> rest_framework 가 자동완성이 안되길레 사용한 방법

</details>

<details>
<summary>#10.4 POST Requests (12:34)</summary>

**GET 요청**

`/categories` 는 모든 카테고리를 보여준다. 하나만 보여주기 위해서 primary key 값을 url 뒤에 넣어서 만들어줄 것이다.

`/categories/1` 로 들어가면 pk값이 1인 카테고리를 보여준다.

먼저 urls.py에 `path("<int:pk>", views.category)` 추가한 후 views.py에 `category`함수를 만들어준다.

```
@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
```

![img](./readme_img/10.4-1.jpg)

정보를 조회하기 위한 GET요청에 관하여 처리하였다.

**POST 요청**

views.py에 `@api_view()` 괄호 부분에 `["GET","POST"]` 단순히 추가만 해줘도 POST 요청까지 한번에 처리해줄 수 있다.

```
@api_view(["GET","POST"])
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories,many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
```

![img](./readme_img/10.4-2.jpg)

심지어 아래부분에 POST요청을 위한 form도 제공해주는 것을 볼 수 있다.

그리고 코드를 request 유형에 따라 수정한후 웹페이지 아래에 있는 `POST` 버튼을 클릭하면 요청이 성공하는 것을 확인해볼 수 있다.

```
@api_view(["GET","POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        return Response({'created':True})
```

![img](./readme_img/10.4-3.jpg)

만약에 유저로부터 POST요청을 받는 경우를 상세히 코드로 짜보려 한다.

```
{
"name": "test from 웹페이지 !!",
"kind": "rooms"
}
```

위 내용으로 post를 보내면 올바른 형식을 인지하고 요청이 성공하게 된다.

이 정보로 바로 데이터베이스를 수정하게 되면 편하겠지만 검증과정을 거치는 것이 좋다.

그리고 Serializer는 파이썬 객체를 json user word로 바꿔주는 것 뿐만 아니라 반대의 경우인 유저의 json user word를 파이썬 객체로 번역하는 것도 해준다!


</details>

<details>
<summary>#10.5 is_valid() (09:43)</summary>

**검증하기**

Serializer가 유저가 POST요청을 보낸 데이터를 검증하는데 도움을 줄 수 있다.

Serializer에게 파이썬 객체를 JSON으로 번역시키고 싶으면 인스턴스를 첫번째 인자로 주면된다.

`serializer = CategorySerializer(all_categories,many=True)`

Serializer에게 유저가 보낸 JSON을 파이썬 객체로 번역시키고 싶으면 `data=~~~`을 사용하면 된다.

`serializer = CategorySerializer(data=request.data)`

serializer에게 데이터의 형태를 미리 알려줬기 때문에 미리 알려준 데이터 형식을 알고 있다.

```
elif request.method == "POST":
    serializer = CategorySerializer(data=request.data)
    print(serializer.is_valid())
    print(serializer.errors)
    return Response({'created':True})
```

`is_valid()`로 검증해볼 수 있다. `errors`로 오류의 내용을 알아낼 수 있다.

 serializer를 한번 만들어뒀다면 파싱과 검증까지 모두 할 수 있다.

```
from rest_framework import serializers

class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True) 
    name = serializers.CharField(required=True,max_length=50,)
    kind = serializers.CharField(max_length=15,)
    created_at = serializers.DateTimeField(read_only=True)
```

serializer를 이렇게 수정함으로써 pk, created_at를 유저가 post요청하지 못하게 할 수 있고, name, kind의 값에 제한을 걸 수 있다.

```
@api_view(["GET","POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            return Response({'created':True})
        else:
            return Response(serializer.errors)
```
검증 결과를 기준으로 if문으로 경우를 나눠 성공과 실패(오류 리턴하기)를 나눴다.


</details>


<details>
<summary>#10.6 save() (12:22)</summary>

**데이터베이스에 저장하기**

카테고리는 2가지 방과 활동으로 선택 제한이 걸려있다.

```
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True) 
    name = serializers.CharField(required=True,max_length=50,)
    kind = serializers.ChoiceField(max_length=15,choices=Category.CategoryKindChoices.choices,)
    created_at = serializers.DateTimeField(read_only=True)
```
serializers를 위와 같이 수정한다. kind를 `ChoiceField`로 바꾼후 기존에 만들어둔 카테고리 모델의 kind 선택 클래스를 이용한다.

model과 serializers에게 2번씩 데이터를 정의해주는 것은 번거로운 과정이다.

serializer는 `save()` 메서드가 있다. 이 메서드를 작동시키면 create메서드를 찾기 시작한다. 이 `create`메서드는 직접 만들어줘야한다.

`create`메서드는 새로운 객체를 return하거나 error를 return해줘야 한다.

```
def create(self, validated_data):
    return Category.objects.create(
        name=validated_data['name'],
        kind=validated_data['kind']
    )
```

이렇게 만드는 것은 비생산적이다.

```
def create(self, validated_data):
    return Category.objects.create(**validated_data)
```
이렇게 간단하게 적어주면 똑같은 효과를 얻을 수 있다.

```
if serializer.is_valid():
    new_category=serializer.save()
    return Response(CategorySerializer(new_category).data,)
```
검증후 코드를 이렇게 적어주고 화면에 POST결과를 띄워줄 수 있다.

![img](./readme_img/10.6-1.jpg)

![img](./readme_img/10.6-2.jpg)

화면에서 성공한 결과를 볼 수있고 데이터베이스에 정상적으로 값이 들어가는 것을 볼 수 있다.

GET, POST 요청 완료하였다. 앞으로 수정PUT과 삭제DELETE도 진행할 것이다.

</details>

<details>
<summary>#10.7 update() (17:19)</summary>

**업데이트하기**

```
@api_view(["GET","PUT"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = CategorySerializer(
            category, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
```

카테고리 세부 항목에서 PUT메서드로 수정 할 것이다. 먼저 PK값으로 카테고리 세부항목을 가져오니 존재하면 항목을 가져오고 없다면 404 NOT FOUND를 띄우도록 초반에서 설정을 해줬다.

그리고 처음에는 GET메서드일 경우 간단하게 보여주는 코드이고 그 다음에 PUT메서드로 수정할때의 코드이다.

수정할때는 name과 kind를 모두 수정할 수도 있지만 그중 하나만 수정할 경우도 있다. 따라서 둘중 하나만 수정할 경우를 위해 `partial=True`를 추가하여 수정하고 싶지 않은 나머지 항목은 처음값 그대로 유지되게 한다.

PUT메서드에서 사용하는 `serializer.save()`는 Serializer의 `update`함수를 찾으러 간다. 따라서 `update`함수를 직접 구현해줘야한다.

```
def update(self, instance, validated_data):
    instance.name = validated_data.get("name",instance.name)
    instance.kind = validated_data.get("kind",instance.kind)
    instance.save()
    return instance
```

update는 에서는 instance인자를 통해 바뀐값을 수정해줘야한다. 여기서 `.get()`메서드를 사용하는데 이 메서드의 두번째 인자는 찾고하하는 첫번째 인자가 존재하지 않으면 기본값을 대신 반환한다는 의미이다. 따라서 기본값으로 처음 값 그대로를 반환해주기 위해 `instance.~~`를 사용해준다.

값을 바꿔줬으면 `instance.save()`로 저장해주고 instance를 반환해준다.

그리고 화면에 instance 값을 띄워준다.

</details>

<details>
<summary>#10.8 DELETE (05:05)</summary>

**삭제하기**

`@api_view(["GET","PUT", "DELETE"])`

삭제를 위해 method를 추가해준다

`from rest_framework.status import HTTP_204_NO_CONTENT`

```
elif request.method=="DELETE":
    category.delete()
    return Response(status=HTTP_204_NO_CONTENT)
```

204 response를 띄우기 위해 임포트 해오고 단순하게 `category.delete()`로 삭제해준다.

`path('api/v1/categories/', include('categories.urls')),`

그리고 api URL주소를 다음과 같이 `api/v1/categories/`로 바꿔주어 api관련 주소임을 적어주는 것이 좋다. 그리고 api 버전도 적어주는것이 좋다.

</details>


<details>
<summary>#10.9 Recap (08:55)</summary>

**복습**

- 프론트는 리액트를 쓰고 장고는 백엔드 api로만 사용할 것이다.
- 장고 serializer를 사용한다.
- 장고 rest 프레임워크를 사용한다.
- serializer에서 제한을 걸어줄 수 있다.
- 번역해야할 것이 있다면 many 인자를 사용해준다.
- serializer는 인자를 받아 요청 메서드를 수행한다.
- 검증절차를 수행할 수 있다.
- 데이터베이스 작성, 수정, 삭제를 할 수 있다.
- serializer 내부에 생성, 수정 함수를 구현해야한다.
- 항상 데이터가 유효한지 검증하고 수행해줘야한다.
- 
</details>

<details>
<summary>#10.10 APIView (10:00)</summary>

**APIView를 통한 리팩토링**

```
from categories.serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Category

class Categories(APIView):

    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category=serializer.save()
            return Response(CategorySerializer(new_category).data,)
        else:
            return Response(serializer.errors)

class CategoryDetail(APIView):

    def get_object(self,pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
        return category

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk), 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
```

리팩토링 후의 코드이다.
if~else문들을 없애버리고 각각의 get, post, delete, put 메서드들을 클래스 속의 함수들로 바꾸어 주었다.

그리고 try except문으로 카테고리 세부정보 가져올때 해당 카테고리의 존재 유무를 판단했었는데 장고의 관습적인 방법을 사용하였다. `get_object`함수를 만들어 판단하고 `category`라는 값으로 return하였다. 아래 함수들에서 이 값을 사용할 때에는 `self.get_object(pk)`로 가져온다.

```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Categories.as_view()),
    path("<int:pk>", views.CategoryDetail.as_view())
]
```

마지막으로 url을 다음과 같이 수정해준다. 클래스로 만들어줬기 때문에 `views.Categories.as_view()`로 가져온다.

</details>

<details>
<summary>#10.11 ModelSerializer (11:53)</summary>

**ModelSerializer로 중복 줄이기**

ModelSerializer으로부터 serializer를 상속받으면 이때까지 구현했던 것들을 다 제공받을 수 있다.

상속받은 클래스 안에 Meta클래스를 만들어 사용하고자하는 Model과 표시하고자하는 필드를 선택해줄 수 있다.

```
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "pk",
            "name",
            "kind",
        )
```
필드는 표시하고싶은것, `exclude`를 사용하면 제외하고 싶은것만 적을 수도 있다.`fields="__all__"` 이렇게 적으면 모든 필드를 표시할 수 있다.

</details>

<details>
<summary>#10.12 ModelViewSet (07:34)</summary>

**ModelViewSet로 중복 줄이기**

```
from categories.serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category

class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

```

`ModelViewSet`을 이용하면 단 2줄로 모든 기능을 사용할 수 있다.

대신 urls.py에서 어떤 request 메서드를 사용할 것인지만 정해주어야 한다.

```
from django.urls import path
from . import views
urlpatterns = [
    path('', views.CategoryViewSet.as_view({
        'get':'list',
        'post':'create',
    })),
    path("<int:pk>", views.CategoryViewSet.as_view({
        'get':'retrieve',
        'put':'partial_update',
        'delete':'destroy',
    }))
]
```

`views.CategoryViewSet.as_view()`안에 요청 메서드와 해당 메서드의 함수를 짝지어 주면 된다.

[장고 rest 프레임워크의 viewset](https://www.django-rest-framework.org/api-guide/viewsets/#viewsets)

</details>

<details>
<summary>#10.13 Conclusions (09:36)</summary>

**ModelViewSet를 사용하지 않는 이유**

ModelViewSet보더 다 나은 방법은 장고가 제공하는 routing을 사용하는 것인데 이미 ModelViewSet 방법부터 너무 많은 것들이 추상화가 되어있다는 단점이 있다. 세부적으로 가능을 손봐야할 경우나, 기능이 어떻게 동작하는지 알아볼 수 없을 정도로 추상화되어 있어서 짜야할 코드는 짧을 수 있지만 불편할 수 있다.

따라서 ModelViewSet은 사용하지 않을 예정이다.

</details>

<details>
<summary>#11.0 All Amenities (12:38)</summary>

**Amenities 구현하기**

APIView 까지의 기능을 사용하여 손쉽게 구현한다.

여기서 serializer을 만들때 부모 클래스인 `ModelSerializer`로부터 상속받아 사용하는데 `id, created_at, updated_at`는 자동으로 `read_only`가 적용되어 편리하다.(직접 구현해주지 않아도 된다.)

amenity에 관한 구현을 계속 진행할 것이다.

</details>

<details>
<summary>#11.1 Amenity Detail (07:13)</summary>

**Amenities 구현하기**

Amenity detail의 get, put, delete 기능구현

</details>

<details>
<summary>#11.2 Perks and PerkDetail (12:00)</summary>

**Perk 구현하기**

Perks의 get, post기능구현과 Perk detail의 get, put, delete 기능구현

</details>

<details>
<summary>#11.3 Rooms (12:23)</summary>

**rooms 구현하기**

방을 보는건 인증 상관 없지만 방을 생성하려면 로그인된 인증 상태여야 한다.

```

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1
```

serializer를 만들 때 `depth=1`를 사용하게 되면 데이터 베이스의 관계를 한단계 깊이 표현하여 관계가 있는 객체의 세부 정보까지 한칸 깊게 보여준다.

![img](./readme_img/11.3-1.jpg)

하지만 모든 것이 필요한 경우는 잘 없고 많은 불필요한 데이터를 가져오는 것은 비효율적이다.

우리는 owner의 세부정보들은 room/1 처럼 방의 세부정보를 보려고 할때 보여줄 것이다.

따라서 serializer를 수정해줘야한다.

</details>

<details>
<summary>#11.4 Room Detail (14:42)</summary>

**rooms의 serializer 구현하기**

세부 방의 정보를 보여줄 때 owner의 정보를 depth=1으로 설정하게 되면 보안에 염려되는 정보까지 공개가 될 수 있다. 따라서 user에 직접가서 serializer를 만들어주어 보여주고 싶은 것들만 보여주도록 한다.

```
from rest_framework.serializers import ModelSerializer

from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name","avatar","username",
        )
```
미리 작은 정보만 보여주는 serializer를 유저에 만들어두고, 이것을 room의 serializer를 만들때 활용한다.


```
class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer()
    amenities = AmenitySerializer(many=True)
    category = CategorySerializer()
    class Meta:
        model = Room
        fields = "__all__"
```

그런다음 방의 세부정보 serializer를 만들때 import해와서 사용해준다. 그러면 우리가 보여주고 싶었던 부분만 보여줄 수 있다.

나머지 amenities, category또한 relation으로 연결되어 있어 그냥 pk 값으로만 보여졌었지만 각각의 serializer를 가져와서 연결지어주면 `depth=1`를 사용하지 않고 한층 더 깊게 데이터를 가져올 수 있다. 또한 각각의 항목들에서 보여주고 싶지 않은 부분은 각각의 serializer에서 fields값을 적절히 수정하면 된다.

같은 파일에 있는 serializer를 사용하고 싶다면 사용 당하는 serializer가 더 위에 있으면 된다.

</details>

<details>
<summary>#11.5 Create Room (11:41)</summary>

**만들어본 api로 room생성해보기**

방을 생성할 때 가장 걸림돌이 되는 것은 relation이 있는 정보를 넘겨줘야할 때이다.

owner, amenities, category가 있는데 그중에서 owner를 먼저 다룰 것이다.

owner는 유저가 조작할 수 없도록 request.data로부터 받지 않도록 할 것이다. 만약 request.data로부터 받으면 유저가 request를 조작하여 다른사람이 방을 만든것으로 할 수 있기 때문에 그런 상황을 피해야 한다.

serializer에서 `owner = TinyUserSerializer(read_only=True)` 이렇게 읽기 전용으로 바꾸어 입력값을 무시하도록 한다.

만약 category, amenities의 각각의 serializer가 요구하는 입력형식을 만족하였지만 각각에 존재하는 category, amenities를 입력해줘야 정상적으로 room을 생성하는 과정으로 취급된다. 존재하지 않는 값들을 넣게 되면 serializer.is_valid()는 문제가 없다고 통과시키지만 db에 저장하는 과정에서 오류가 생기게 된다.

```
{
    "owner":1,
    "category":{"name":"wwwwwwwssssss","kind":"rooms"},
    "amenities":[{"name":"asdfasdfasdfa","description":"eeeeeeee"}],
    "name": "house created by DRF",
    "country": "한국",
    "city": "제주",
    "price": 3000,
    "rooms": 2,
    "toilets": 2,
    "description": "많이 비쌈...",
    "address": "제주 서귀포시",
    "pet_friendly": true,
    "kind": "private_room"
}
```

이런식의 입력을 넣고 POST를 하면 

```
AssertionError at /
The `.create()` method does not support writable nested fields by default.
Write an explicit `.create()` method for serializer `rooms.serializers.RoomDetailSerializer`, or set `read_only=True` on nested serializer fields.
```
이런 오류가 발생하게 된다.

</details>

<details>
<summary>#11.6 Room Owner (13:13)</summary>

**만들어본 api로 room생성해보기 - owner**

POST요청의 serializer.save() 코드가 create함수를 호출하게 된다. category, amenities둘다 read_only로 바꿔주면 오류를 회피하였지만, 필수적인 요소가 빠졌다고 새로운 오류가 뜬다.

여기서 유저 정보를 받아오기 위하여 request.data가 아니라 request object의 정보를 사용하여 현재 post요청을 하는 유저가 누구인지 알아낼 수 있다. (`request.user`)

```
if request.user.is_authenticated:
    serializer = RoomDetailSerializer(data=request.data)
    if serializer.is_valid():
        room = serializer.save()
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
else:
    raise NotAuthenticated
```

request.user의 인증 여부에 따라 코드를 짜줄 수 있다.

![img](./readme_img/11.6-1.jpg)

`room = serializer.save(owner=request.user)` 저장할때 매개변수로 owner를 직접 지정해준다면 create 메서드가 동작할때, validated_data에 자동으로 매개변수로 넣어준 owner를 추가해준다. 이 방법을 사용하면 간편하게 create메서드를 오버라이딩할 필요없이 필요한 정보를 추가해줄 수 있다.

그리고나서 POST요청을 하면 정상적으로 요청이 성공한다. 물론 category, amenities가 없는 상태로 되었다.

![img](./readme_img/11.6-2.jpg)

</details>

<details>
<summary>#11.7 Room Category (09:54)</summary>

**만들어본 api로 room생성해보기 - category**

카테고리 처리를 해주기 위해서 카테고리를 필수로 적어야 하는지 여부에 대하여 우리가 정해줘야한다. 필수로 적어야 한다고 생각하고 구현하도록 한다.

```
category_pk = request.data.get("category")
    if not category_pk:
        raise ParseError
```

먼저 request.data 값에 카테고리를 넣었는지 확인한다. 카테고리가 없다면 오류를 띄운다. `ParseError` 는 400 bad request 를 화면에 띄워준다.

```
try:
    category = Category.objects.get(pk=category_pk)
    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
        raise ParseError
except Category.DoesNotExist:
    raise ParseError
room = serializer.save(
    owner=request.user, 
    category = category,)
```

그런 다음 try~except문으로 존재하는 카테고리라면 성공적으로 데이터를 저장시킬 것이고, 그렇지 않으면 ParseError을 띄울 것이다. 또한 room에 대한 생성이므로 Experience 형태의 생성은 ParseError을 띄워 막아줄 것이다.

검증이 끝났으면 카테고리의 pk값을 serialize.save의 인자로 넣어준다. 

여기서 카테고리의 pk 값은 프론트에서 유저에게 선택권을 주어 pk값을 즉시 받을 수 있도록 구현해야할 것이다.

</details>

<details>
<summary>#11.8 Room Amenities (14:26)</summary>

**만들어본 api로 room생성해보기 - amenities**

ParseError오류는 오류의 이유를 적어줄 수 있다.

```
category_pk = request.data.get("category")
if not category_pk:
    raise ParseError("Category is required.")
try:
    category = Category.objects.get(pk=category_pk)
    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
        raise ParseError("The category kind should be 'rooms'")
except Category.DoesNotExist:
    raise ParseError("Category not found.")
```

방을 생성하려면 owner가필요하다. User 모델을 통해 유저를 찾아내어 owner에 할당한다.

category도 필요하다. 마찬가지로 Category모델을 통해 카테고리를 찾아내어 category에 할당한다.

owner, category는 ForiegnKey로 받아오기 때문에 하나씩 대응이 되면 된다. 하지만 amenities는 ManyToManyField 이기 때문에 여러개가 들어올 수 있고, 아무것도 없어도 된다.

따라서 amenities는 add()방식으로 하나씩 추가해주고 remove() 방식으로 삭제를 해줘도 된다.

```
amenities = request.data.get("amenities")
for amenity_pk in amenities:
    try:
        amenity = Amenity.objects.get(pk=amenity_pk)
        room.amenities.add(amenity )
    except Amenity.DoesNotExist:
        raise ParseError(f"Amenity with id {amenity_pk} not found")
```

amenity가 입력되던 중간에 존재하지 않는 것이 입력되면 어떻게 할건지 여러 방법이 있다. 위 코드처럼 잘못된것이 입력되었다고 알려주면서 방은 정상적으로 생성해주는 방법이 있고, raise부분을 pass로 처리해버려 그냥 조용히 지나가는 방법이 있고, room을 아예 delete해버리는 방법도 있다.

</details>

<details>
<summary>#11.9 Transactions (08:58)</summary>

**transaction**

amenities 들을 입력하다가 존재하지 않는 amenity가 식별되면 만들던 room을 삭제해버리는 경우가 있을 것이다. 이 경우 room을 한번 생성했다가 삭제하는 과정을 거치기 때문에 room의 id가 계속 +=1 이 된다.

여러번 생성 삭제를 반복하다가, 드디어 정상적으로 방이 생성된 상황이라면 id값이 몇칸 뛰어넘은 상태가 된 것을 볼 수 있다. 이런 경우를 위하여 장고는 transaction기능을 제공해준다.

실패했다면 모든 과정을 전부 실패로, 성공했다면 모든 과정을 전부 성공으로.

`from django.db import transaction`

```
class Rooms(APIView):

    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):

        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if not category_pk:
                    raise ParseError("Category is required.")
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'")
                except Category.DoesNotExist:
                    raise ParseError("Category not found.")
                # 트랜색션 시작
                try:
                    with transaction.atomic():
                        room = serializer.save(
                            owner=request.user, 
                            category = category,)
                        amenities = request.data.get("amenities")
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity )
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Amenity not found")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated
```

전체 코드에서 데이터베이스에 본격적으로 저장되는 부분이 트랜색션 시작부분부터 try except문으로 시작한다.
일단 오류가 나면 유저에게 알려주기 위함이다. 그리고 오류가 발생하면 `with.transaction.atomic()`부분으로 전체 과정이 감싸져있기 때문에 중간에 amenity로 인하여 오류가 발생한다면 전체 과정을 없었던 시점으로 되돌린다.

</details>

<details>
<summary>#11.10 Delete Rooms (09:26)</summary>

**room delete기능**

delete기능 생성

```
def delete(self, request, pk):
    room = self.get_object(pk)
    if not request.user.is_authenticated:
        raise NotAuthenticated
    if room.owner != request.user:
        raise PermissionDenied
    room.delete()
    return Response(status=HTTP_204_NO_CONTENT)
```

삭제시 유저가 누구인지 여부가 중요하기 때문에 해당 부분에 대하여 검사를 먼저하고 삭제해준다.

put기능을 스스로 만들어보는 과제!

기본적으로 delete처럼 유저가 누구인지 여부를 먼저 판단하고 진행한다.

```
serializer = RoomDetailSerializer(room, data=request.data,partial=True)
        if serializer.is_valid():
            # category_kind must be room
            category_pk = request.data.get('category')
            if category_pk:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError("The category kind should be 'rooms'")
                except Category.DoesNotExist:
                    raise ParseError("Category not found.")
            # Amenities with transaction
            try:
                with transaction.atomic():
                    # 1. category update
                    if category_pk:
                        updated_room = serializer.save(category = category)
                    else:
                        updated_room = serializer.save()

                    # 2. amenities update
                    amenities = request.data.get('amenities')
                    if amenities:
                        # 2.1 update = delete + post
                        room.amenities.clear()
                        
                        for amenity_pk in amenities:
                            amenity = Amenity.objects.get(pk=amenity_pk)
                            room.amenities.add(amenity)
                    else:
                        room.amenities.clear()

                    return Response(RoomDetailSerializer(room).data)
            except Exception:
                print(Exception)
                raise ParseError("Amenity not found")
        else:
            Response(serializer.errors)
```

[코드참고](https://github.com/daveg7lee/airbnb-clone-backend/commit/b50b15dba46877a5afb64832423dc6cc5cce4491)

</details>

<details>
<summary>#11.11 SerializerMethodField (07:32)</summary>

**serializer에 추가필드 넣기**

`from rest_framework import serializers` 를 먼저 임포트 해온 뒤, `RoomDetailSerializer` 내부 `Meta` 클래스 위에 다음 코드를 만들어준다.

```
rating = serializers.SerializerMethodField()

def get_rating(self, room):
    return room.rating()
```

여기서 rating에 관한 메서드를 만들어 줄때는 반드시 `get_`+`이름` 형식으로 만들어줘야한다. 그리고 메서드는 인자를 2개를 받는다. Meta에 지정해준 모델클래스가 만든 객체를 자동으로 인자로 받는다.

`RoomListSerializer`에도 똑같은 rating기능을 만들어 주려면 같은 코드를 적어주면 된다. 여기서 fields에 추가도 해줘야 보이게 된다.

```
class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, room):
        return room.rating()
    class Meta:
        model = Room
        fields = ("pk","name","country","city","price","rating")
```

</details>

<details>
<summary>#11.12 Serializer Context (06:43)</summary>

**context인자로 serializer에게 원하는 내용 전달하기**

`serializer = RoomDetailSerializer(room,context={"request":request},)`

views.py의 get메서드의 serializer에 context인자로 request를 주고, 

```
is_owner = serializers.SerializerMethodField()

def get_is_owner(self,room):
    request = self.context["request"]
    return room.owner == request.user
```

serializer에서 위 코드처럼 메서드를 만들어 방의 주인과 현재 로그인한 유저가 같은지 확인할 수 있게 하는 메서드를 만들 수 있다.

이런 기능을 해당 유저가 좋아요를 눌렀는지 아닌지 확인할 때 사용할 수 있다.

</details>

<details>
<summary>#11.13 Reverse Serializers (08:13)</summary>

**역접근자 serializer**

reverse accessor는 외래키를 통해 연결되어 있는 것들을 역접근자로 찾아내는 방법이다.

각 방들의 리뷰들을 역 접근 serializer로 접근해보도록 하겠다.

먼저 리뷰의 serializer를 간단히 만들어 놓는다.

```
from rest_framework.serializers import ModelSerializer

from .models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
```

그런다음 room의 serializer으로 돌아와 `reviews = ReviewSerializer(many=True, read_only=True)`를 추가해주면 리뷰들을 볼 수 있다.

역접근자 덕분에 room.views 뿐만으로 review까지 접근할 수 있다.

하지만 방 하나는 수만개 이상의 리뷰를 가질 수 있기 때문에 엄청난 자원낭비를 초래할 수 있다. 그래서 Pagination 기능을 사용할 수 있다.

</details>

<details>
<summary>#11.14 Pagination (18:37)</summary>

**리뷰 페이지 기능**

역접근자로 리뷰를 가져오게되면 리뷰의 개수가 너무 많은 상황에서 데이터베이스에게 엄청난 부담이 될 수 있다. 따라서 URL을 하나 더 파서 페이지마다 리뷰가 나오게 만들 것이다.

`path("<int:pk>/reviews",views.RoomReviews.as_view()),`

```
class RoomReviews(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = ReviewSerializer(room.reviews.all(),many=True,)
        return Response(serializer.data)
```

url을 추가하고 방 리뷰만 가져오게 리뷰 클래스를 만들어준다.

url에 쿼리로 `reviews?page=2` 이런식으로 몇번 페이지인지 받고 그 페이지를 보여줄 것이다. 먼저 페이지 번호를 검증하고 가져온다.

```
try:
    page = request.query_params.get("page",1)
    page = int(page)
except ValueError:
    page = 1
```

검증 후 페이지 크기에 따라 리뷰들을 보여준다.

```
page_size = 5
start = (page-1)*page_size
end = start+page_size
room = self.get_object(pk)
serializer = ReviewSerializer(room.reviews.all()[start:end],many=True,)
```

room.reviews.all()을 리스트로 가져오기때문에 start ~ end로 슬라이싱이 가능하다.
슬라이싱하면 자동으로 장고는 db로 sql offset ~ limit문을 전송한다.

</details>

<details>
<summary>Amenities 페이지 기능 만들기</summary>

**Amenities 페이지 기능**

장고의 paginatorl 모듈을 이용하여 더 편하게 만들 수 있다.

마지막 페이지에 남는 몇개의 항목들은 마지막에 붙여서 더 길게 만들어줄 수도 있다.(orphans인자)

마지막 페이지보다 더 큰 수가 입력되면 가장 마지막 페이지를 보여주기도 한다.


</details>

<details>
<summary>#11.15 File Uploads (12:37)</summary>

**사진 파일 업로드**

이미 만들어둔 Photo 모듈로 사진을 업로드 하게되면 우리 프로젝트 파일안에 대충 생성되게 된다. 

config > settings.py에 가서 설정을 해줌으로 파일이 저장될 폴더를 만들어주고 경로를 지정해줄 수 있다. 그리고 사진 파일에 접근할 때 URL경로도 지정해줄 수 있다.

```
MEDIA_ROOT = "uploads"

MEDIA_URL = "user-uploads/"
```

세팅 파일에 위 코드를 만들어준다

`from django.conf import setting` 로 setting의 변수들을 가져올 수 있다. api 토큰같은 것을 저장하여 변수로 사용가능하다.

```
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("rooms.urls")), # 임시
    path('admin/', admin.site.urls),
    path('api/v1/rooms/', include("rooms.urls")),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/experiences/',include('experiences.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
```

위 2개 모듈을 먼저 임포트 해오고 전역으로 세팅파일에서 만들었던 이미지 저장경로와 API URL을 가져온다.

이 방식을 추가적으로 pagination에서 page size를 지정해주는 방법으로 활용할 수 있다.

하지만 이 방법은 보안에 취약하기 때문에 사용하면 안되는 방법이다.

</details>


<details>
<summary>#11.16 Upload Photo (10:31)</summary>

**사진 업로드**

다른 서버로 사진을 업로드 하는 방법을 사용하면 보안문제 해결가능하다.

파일은 클라우드에 올릴 예정이라 Media의 FileField를 UrlField로 바꿀 것이다.

사진을 업로드 할수 있는 유저의 검증을 곁들여 post요청을 마무리 짓는다. 먼저 photo serializer를 만든다.

```
from rest_framework.serializers import ModelSerializer
from .models import Photo

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ("pk","file","description",)
```

그리고 이것을 이용하여 완성한다.

```
class RoomPhotos(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if request.user != room.owner:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(room=room)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
```

</details>

<details>
<summary>#11.17 permission_classes (13:22)</summary>

**사진 삭제, 검증된 유저 클래스**

사진을 삭제할때 room으로부터 삭제하는지, media로부터 삭제하는지 정해야 한다.

media로부터 삭제하도록 한다. url을 추가하고 view를 만들어준다.

```
if not request.user.is_authenticated:
    raise NotAuthenticated
```

이 부분은 유저가 검증된 상태인지 확인하는 것인데 많이 반복된다.

`from rest_framework.permissions import IsAuthenticated`을 가져와서 `permission_classes = [IsAuthenticated]` 를 클래스 안에 선언해놓으면 위 코드를 생략할 수 있다.

</details>
<details>
<summary>#11.18 Reviews (10:39)</summary>

**리뷰 기능 만들기**

rooms/1/reviews 경로로 post api를 만드는 것이 /api/v1/reviews/~ 처럼 만드는 것보다 더 직관적이고 자세하여서 좋다.

post 요청을 보내기 위해 검증을 받아야 한다. `permission_classes = [IsAuthenticatedOrReadOnly]`를 추가해준다.

rooms 경로부터 리뷰를 생성하기 때문에 serializer에서 유저와 payload, rating 필드만 보여줘야한다. 필드를 `fields = ("user","payload","rating",)`수정한다. 그리고 유저가 foreign key로 묶여있기 때문에 `user = TinyUserSerializer(read_only=True)` 로 유저의 정보를 조금 보여주도록 한다.

```
def post(self, request, pk):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = serializer.save(user=request.user,room=self.get_object(pk),)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
```

post기능을 완료한다.

</details>
<details>
<summary>#11.19 Wishlists (13:26)</summary>

**위시리스트 만들기**

모든 위시리스트를 가져올 필요없이 해당 유저의 것만 가져오기 위해 filter를 사용한다.

`context={"request":request},`

wishlist의 serializer, urls, views를 만들어준다.

`rooms = RoomListSerializer(many=True, read_only=True,)` serializer를 만들때 이 코드를 사용하여 해당 유저의 방을 볼 수 있게 한다.

```
def get(self, request):
    all_wishlists = Wishlist.objects.filter(user = request.user)
    print('request.user',request.user)
    serializer = WishlistSerializer(all_wishlists,many=True,context={"request":request},)

    return Response(serializer.data)
```

정보를 가져올때, context인자를 가져와야한다. RoomListSerializer는 필요로하는 인자이기 때문이다.

</details>

<details>
<summary>#11.20 Wishlist (17:12)</summary>

**위시리스트 세부기능 만들기**

로그인한 유저의 위시리스트만 보여줘야 함에 주의한다. 그리고 위시리스트의 세부정보를 가져올때는 serializer에 context={"request": request}, 를 포함시켜줘야한다.

위시리스트를 수정하는 기능을 위해서는 `위시리스트 번호/rooms/방번호` 형식으로 만드는 것이 변수를 활용하기 좋다.

```
class WishlistToggle(APIView):

    def get_list(self,pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound
    
    def get_room(self,pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    
    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)

        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(status=HTTP_200_OK)
```

위시리스트에 put메서드로 요청을 보내면 2가지 기능중 하나가 동작한다.

1. 만약 위시리스트에 존재하지 않는 방이라면 방을 위시리스트에 추가한다.
2. 위시리스트에 이미 존재하는 방이라면 방을 위시리스트에서 삭제한다.

</details>


<details>
<summary>#11.21 is_liked (06:59)</summary>

**좋아요 기능 만들기**

ManyToMany 필드에 필터를 사용할 때 쉬운 방법이 있다.
먼저 우리가 찾고자 하는 유저의 모든 위시리스트를 가져온 다음 그 위시리스트에서 우리가 찾고자 하는 방의 번호를 찾고싶은 상황이 있다.

```
def get_is_liked(self,room):
    request = self.context['request']
    return Wishlist.object.filter(
        user=request.user,
        rooms__pk=room.pk
        ).exists()
```

`__`를 사용하여 방의 pk뿐만 아니라 이름을 이용하여 필터를 넣을 수 있다.

</details>

<details>
<summary>#11.22 Bookings (16:34)</summary>

**예약 기능 만들기**

예약은 기간이 존재한다. 예약이 잡힌 방은 예약된 기간동안 다른사람이 예약하지 못하도록 제한을 걸어야 한다.

```
def get_object(self, pk):
    try:
        return Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        raise NotFound

def get(self, request, pk):
    room = self.get_object(pk)
    bookings = Booking.objects.filter(room=room)
```

이 코드는 방이 존재하지 않는다면 유저에게 알려준다.

```
def get(self, request, pk):
    bookings = Booking.objects.filter(room__pk=pk)
```

이 코드는 위 코드위 동일한 기능이지만 방이 존재하지 않아도 bookings변수에 빈 리스트를 저장하는 것으로 끝나기 때문에 유저에게 방 존재여부를 알려주지 않는다. 따라서 어떻게 할지 정해볼 수 있다.

Booking의 시리얼라이저를 만드는데 일반 유저가 볼 public버전과 방 주인이 볼 pivate 버전 2개를 만들 것이다.

```
from rest_framework.serializers import ModelSerializer
from .models import Booking

class PublicBookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ("pk",
                "check_in",
                "check_out",
                "experience_time",
                "guests",
                )
```

`from django.utils import timezone` 을 사용하여 날짜+시간을 사용한다. 파이썬 기본 모듈보다는 장고의 모듈을 사용하는 것이 config파일의 setting을 활용할 수 있어서 좋다.


```
class RoomBookings(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        now = timezone.localtime(timezone.now())

        bookings = Booking.objects.filter(room=room,
            kind=Booking.BookingKindChoices.ROOM,
            check_out__gt=now,            
            )
        serializer = PublicBookingSerializer(bookings, many=True)
        return Response(serializer.data)
```

config에 명시한 서버 로컬 시간에 맞추기 위해서 `now = timezone.localtime(timezone.now()).date()` 처럼 코드를 짜주고 날짜만 필요한 경우 `.date()`로 날짜만 가져온다. 시간도 중요하다 생각하면 date빼줘도 된다.

그리고 지금 시간보다 과거의 booking들은 get요청으로 가져오지 않는다. check_out 기준으로 조금 수정하여 만들었다.

</details>


<details>
<summary>#11.23 Create a Booking (16:55)</summary>

**예약 기능 만들기**

booking의 몇가지 필드들은 조건에 따라 필수가 될 수도, 아닐 수도 있다.

따라서 보여주기용 serializer와 생성용 serializer를 따로 만들는 방법을 사용한다.

room생성 시리얼라이저를 만들고, 체크인, 체크아웃을 필수로 바꿔주기 위해 오버라이딩한다.

```
class CreateRoomBookingSerializer(ModelSerializer):
    
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    
    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
                )
```

본격적으로 booking을 생성하기 전에 몇가지 조건들을 제한해줘야 한다. 시리얼라이저의 `is_valid()`를 믿을 수 없는 조건이 존재한다. 날짜에 대한 조건 설정을 해야한다.

이것을 view에서 만들어 줄 수도 있지만 시리얼라이즈에서 만들어주는 방법도 있다.

serializer에서 now를 가져와서 value와 비교할 수 있는 이유는 둘다 type이 datetime이기 때문에다.

```
class CreateRoomBookingSerializer(ModelSerializer):
    
    check_in = serializers.DateField()
    check_out = serializers.DateField()
    
    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
                )
    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value
```

체크인, 체크아웃이 미래인지 확인하는 검증절차를 serializer에 적었고, 추가적으로 체크인 -> 체크아웃 순서인지, 체크인 하려고 하는 기간에 다른 사람이 체크인 했는지 여부를 통하여 검증 과정을 추가해줘야 한다.


</details>

<details>
<summary>#11.24 Validate Booking (15:51)</summary>

**예약 검증하기**

```
    def validate(self, data):

        # 체크인 시간은 체크 아웃 시간보다 빨라야 한다.
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check in should be smaller than check out.")
        
    
        # 체크인 시간과 체크아웃 시간 사이에 또다른 booking이 존재하면 안된다.
        # 물론 체크인 또는 체크아웃 중 하나라도 걸쳐있는 booking 또한 존재하면 안된다.
        if Booking.objects.filter(
            check_in__lte=data['check_out'],
            check_out__gte=data['check_in']
        ).exists():
            raise serializers.ValidationError('Those (or some) of those dates are already taken.')

        return data
```

2가지 포인트에 대하여 검증해준다.

1. 체크인 시간 < 체크아웃 시간
2. 다른 예약 시간과 겹치면 안된다.

2번 포인트에 대해 필터로 정의해줄 때 까다로운 부분이 있었다. 

1. 원하는 체크인보다 미래에 누군가의 체크아웃 존재
2. 원하는 체크아웃보다 과거에 누군가의 체크인 존재
   
이 2 부분에 대해 검증을 해주면 된다. 그리고 체크아웃 하는 시점에 체크인을 하는 경우가 많다보니 아래처럼 비교할때 equal을 빼줘도 된다.

`if Booking.objects.filter(check_in__lt=data['check_out'],check_out__gt=data['check_in']).exists():`

</details>

<details>
<summary>#11.25 Booking Completed (07:20)</summary>

**예약 기능 완성!**

검증을 view에서 만들어주는 것이 좋은지 serializer에서 validation 함수로 만들어 주는 것이 좋은지 생각해볼 필요가 있다.

마지막으로 post부분의 저장 부분을 완성시킨다. 반드시 채워야 하는 필드들이 존재하기 때문에 저장할때 추가해주고 저장시켜준다.

```
def post(self, request, pk):
    room = self.get_object(pk)
    serializer = CreateRoomBookingSerializer(data=request.data)
    if serializer.is_valid():
        booking = serializer.save(
            room=room,
            user=request.user,
            kind=Booking.BookingKindChoices.ROOM,
        )
        serializer = PublicBookingSerializer(booking)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
```

</details>
<details>
<summary>#12.0 User Profile (14:31)</summary>

**유저기능 개발 시작**

```
class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
```

유저에게 보여줄 상세한 user정보를 위한 serializer를 만들어준다.

`    avatar = models.URLField(blank=True)` 아바타의 이미지는 url로 받아올 예정이므로 바꿔준후 마이그래이션 작업을 해준다.

```
class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user, data=request.data,partial=True,)
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
```

개인계정을 위한 기능 일부 완성

</details>

<details>
<summary>#12.1 Create User (11:52)</summary>

**유저 추가 기능**

먼저 만들었던 `Me`에는 검증 행위를 진행하지 않고 있다. 예를 들면, 이메일을 수정하는데 이미 존재하는 이메일로 수정했을 시 검증을 통해 제한해야하는 상황을 말한다. 이 검증은 이미 serializer가 자동을 하고 있기 때문에 따로 만들어 주지 않아도 된다.


post할때 raw 비밀번호를 그냥 저장하면 안된다. 하지만 django는 자동으로 hash화 해준다.

`user.set_password()` 라는 메서드를 통해 장고에게 hash 화를 맞긴다.

```
class Users(APIView):

    def post(self, request):
        password = request.data.get('password')
        if not password:
            raise ParseError
        
        serializer = serializers.PrivateUserSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
```

</details>
<details>
<summary>#12.2 Change Password (13:21)</summary>

**pw 변경 기능**

```
path('me',views.Me.as_view()),
path('<string:username>',views.PublicUser.as_view()),
```

이 순서 말고 뒤집은 순서로 놔두게 되면, me를 username으로 착각하게 되어 오류가 발생한다. 하지만 me라는 이름을 가진 유저가 등장하게 되면 또 문제가 된다.

따라서 인스타그램처러 유저이름 앞에 `@`를 사용해주는 방식으로 문제를 해결한다.

```
path('@<str:username>',views.PublicUser.as_view()),
path('me',views.Me.as_view()),
```

```
class PublicUser(APIView):
    
    def get(self,request, username):

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise NotFound
        
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
```

public유저를 위한 serializer를 만들어주는 것이 좋다.

`set_password`는 비밀번호를 해시할때만 적용되기 때문에 따로 `.save()`메서드로 저장해줘야한다.

```
class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]
    
    def put(self,request):
        user = request.user
        old_pw = request.data.get('old_password')
        new_pw = request.data.get('new_password')
        if not old_pw or not new_pw:
            raise ParseError
        if user.check_password(old_pw):
            user.set_password(new_pw)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError
```

</details>

<details>
<summary>#12.3 Log In and Log Out (06:46)</summary>

**로그인 기능 만들기**

```
class LogIn(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"ok":'Welcome!'})
        else:
            return Response({"error":"wrong Password"})
```

기본적인 로그인은 다음과 같이 엄청 간단히 만들 수 있다.
핵심적으로 `login(request, user)`를 통해 로그인한다. 

```
class LogOut(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({"ok":"bye~"})
```

로그아웃도 간단히 만들 수 있다.

</details>

<details>
<summary>#13.0 Code Challenge (02:36)</summary>

**Experience 부분 code challenge**

### Experience 체크리스트

- [x] GET /experiences
- [x] POST /experiences
- [x] GET PUT DELETE /experiences/1
- [x] GET /experiences/1/perks
- [x] GET POST /perks
- [ ] GET PUT DELETE /perks/1
- [ ] GET POST /experiences/1/bookings
- [ ] GET PUT DELETE /experiences/1/bookings/2

</details>
