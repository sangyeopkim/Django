# Django Tutorial

## Part 2

### 2.1 데이터베이스 설치
* 데이터베이스 생성
* `python manage.py migrate`
* `migrate` 명령은 `setting.py` 안에`INSTALLED_APPS`에서 데이터베이스 설정과 app과 함께 제공되는 데이터베이스 migrations에 따라, 필요한 데이터베이스 테이블을 생성한다.

### 2.2 모델 만들기
#### 모델 ?
> 모델("model")은 정의한 내용들(데이터들)을 데이터베이스에 저장 해 주는 역할을 한다.

* `Question`, `Choice` 라는 두 개의 모델 생성 
* `Question`은 `question(질문)`, `publication date(발행일)` 을 위한 두 개의 필드를 가짐
* `Choice`는 `choice(선택지)` 와 `vote(표)` 계산을 위한 두 개의 필드를 가짐
* 각 `Choice` 모델은 `Question` 모델과 연관된다.

#### Python 에 코드 입력
* `polls/models.py` 실행

```
from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
```

#### django.db.models.Model
* 각 모델들이 서브클래스로 표현된다는 뜻
* 각 모델은 여러개의 클래스 변수를 가질 수 있음
* 각각의 클래스 변수들은 모델의 데이터베이스 필드를 의미

#### Field
* 데이터베이스의 각 필드는 Field 클래스의 인스턴스로 표현
* `CharField` : 문자 필드를 표현
* `DateTimeField` : 날짜와 시간 필드를 표현
* 각 필드가 어떤 자료형을 가질 수 있는지 Django에 알려줌
* 몇몇 Field 클래스들은 필수 인수가 필요함. 예를 들어, `CharField`의 경우 `max_length`를 입력해야함
* 다양한 선택적 인수들을 가질 수 있음. 예를 들어, `default` 로 하여금 `votes`의 기본값을 `0`으로 설정

#### ForeignKey
* 각각의 `Choice`가 하나의 `Question`에 관계된다는 것을 Django에 알려주는 역할  
* Django 는 `다-대-일`, `다-대-다`, `일-대-일` 과 같은 모든 일반 데이터베이스의 관계들을 지원

### 2.3 모델의 활성화