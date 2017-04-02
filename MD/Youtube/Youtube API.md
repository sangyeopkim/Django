# Youtube API

## 환경 Setting
### API KEY
1. API 콘솔에서 프로젝트 생성  
[API Console](https://console.developers.google.com/iam-admin/projects)

2. 프로젝트 생성 클릭
3. API 종류 선택  
> YouTube Data API
4. 사용자 인증 정보 만들기 클릭
5. API를 호출 할 위치?   
> 웹 서버
6. 엑세스 할 데이터?  
> 공개 데이터
7. API Key 생성됨

**API KEY는 .conf 폴더로 관리**

### Use standard tools for installation
```
pip install --upgrade google-api-python-client
```

