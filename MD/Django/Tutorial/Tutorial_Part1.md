# Django Tutorial

## Part 1

### 1.1 설치된 Django 버전 확인
* `python -m django --version`    

### 1.2 프로젝트 만들기
* 작업 할 폴더 생성 및 작업 폴더로 경로 이동
	1. `mkdir django_tutorial`
	2. `cd django_tutorial`
* 해당 경로에서 프로젝트 생성
	1. `django-admin startproject mysite` 
	2. 해당 경로에서 `mysite` 라는 디렉토리 생성하는 명령
	3. `django-admin` : 관리자 작업을 위한 Django의 명령형 유틸리티

### 1.3 startproject 에서 생성된 파일들

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

* `mysite/` : 단순히 프로젝트를 담는 공간
* `manage.py` : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티
* `mysite/` : Project를 위한 실제 Python 패키지들이 저장되는 공간. 이 디렉토리 내의 이름을 이용하여 project 어디서나 Python 패키지들을 import할 수 있음
* `mysite/__init__.py` : Python 으로 하여금 이 디렉토리를 패키지 처럼 다루라고 알려주는 용도의 단순한 빈 파일
* `mysite/settings.py` : 현재 Django project의 환경/구성을 저장
* `mysite/urls.py` : 현재 Django project 의 URL 선언을 저장. Django 로 작성된 사이트의 "목차"라고 할 수 있음
* `mysite/wsgi.py` : 현재 project를 서비스 하기 위한 WSGI 호환 웹 서버의 진입점

### 1.4 개발 서버
* `manage.py`가 있는 `mysite`로 이동
* `python manage.py runserver`
* `./manage.py runserver`
* 위 두개의 명령어 중 하나로 server 동작 확인 가능  

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

February 03, 2017 - 15:50:53
Django version 1.10, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
* 다음과 같은 출력으로 정상 작동 확인 가능
* 웹 브라우져에서 `http://127.0.0.1:8000/`를 통해 접속 가능
* `python manage.py runserver 8080` 명령어를 통해 내부 IP 포트 변경 가능
* `python manage.py runserver 0.0.0.0:8000` 명령어를 통해 서버의 IP 변경 가능

### 1.5 설문조사 앱 만들기
* app 생성
* `python manage.py startapp polls` 명령어를 통해 `polls` app 생성

* `polls` 디렉토리에 자동 생성 된 파일들

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### 1.6 첫 번째 뷰 작성하기
`polls/view.py` 파일을 열어 python 코드 입력

```
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, World")
```

--
view를 호출하려면 이와 연결된 URL이 있어야 한다.  
이를 위해 URLconf가 사용 된다.  
`polls/urls.py` 파일을 열어 코드 입력/확인

```
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
```
--
project 최상단의 URLconf에서 `polls/urls` 모듈을 바라보도록 설정  
`mysite/urls.py` 파일 오픈  
다음과 같은 코드 추가

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', admin.site.urls),
]
```

* `include()` : 다른 URLconf를 참조할 수 있도록 도와줌  
* 정규표현식에서 끝을 의미하는 `$` 대신 `/`로 끝을 나타냄
* Django가 `include()`를 만나게 되면, 그 지점까지 일치하는 URL의 부분을 잘라내고, 남은 부분을 후속 처리하기 위해 include 된 URLconf로 전달
* `/polls/some/method` 를 요청 받으면, `some/method`가 `polls/urls.py`의 URLconf로 넘어간다.

--

* index view가 URLconf에 잘 연결되었는지 확인
* `python manage.py runserver`  
* 웹 브라우저에서 `http://localhost:8000/polls/` 입력 후 확인 가능 







