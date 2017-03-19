##Git 2


###Terminal 에서 Git 작업
* 해당 경로로 이동 -> cd 경로 이름
* 경로 뒤로 가기 -> cd
* 폴더 생성 -> mkdir 폴더명
* 폴더 삭제 -> rm -rf 폴더명
* 파일 삭제 -> rm 파일명
* 해당 파일 파인더에서 열기 -> open .
* local repository 생성하는 방법 --> git init
* ls -a 명령어로 .git 파일이 생성된 것 확인 가능
* git status 로 파일명 빨간색 확인 (Unstage 상태)
* git add 파일명 -> git stage 로 올려줌
* git status 로 파일명 빨간색에서 변한 것 확인 가능
* commit 입력 -> git commit
* commit 입력 후 저장
* git log -> history 확인
* git -A -> 수정되거나 추가된 파일 한번에 add
* git reset HEAD 파일명 -> 한번에 add 된 파일 중 취소 하려는 파일
* git commit -a - m "내용" -> stage 에 올림과 동시에 commit 작성
* git -a -> 전체 파일 add
* git -m "내용" -> commit 작성
* git clone repository url 주소 -> 지워진 폴더 및 파일  서버에서 복구
* git log -p -> 수정 된 내용 포함하여 보여줌
* git push -> remote repository 로 업로드
* git reset --hard commit 번호 -> commit 번호 시점으로 되돌림
* git reset --hard ORIG_HEAD -> reset 잘못한 시점 전으로 되돌림


###Terminal Vi 명령어
* dd -> 한 줄 지우기
* u -> Ctrl + z
* yy -> 복사
* p -> 붙여넣기
* x -> 한 글자 지우기
* :q! -> 저장 안하고 나가기


###Gitignore -> 쓰레기 파일들을 Git 에서 무시
* gitignore.io
* vi .gitignore
* 사용하는 Tool 전부 입력 (giyiynotr.io 에서 복사 붙여넣기)
* Linux, MacOS, Windows, Python 등...
* 나오는 코드 복사
* Terminal 에서 vi .gitignore 생성
* 복사한 부분 붙여넣기
* Gitignore 은 최초 init 만들자 마자 생성해야함 -> 협업을 위해

### Git 응용
1. 폴더 생성 -> 작업 공간 확보
2. git init -> Local Repository 생성
3. git ignore -> 협업을 위해
4. git status 로 .gitignore 생성(빨강) 확인
5. git add -A
6. Initial commit = 최초의 커밋
7. git status 로 확인
8. branch 만들기 -> git branch html (atom index.html 로 open)
9. git branch css
10. git branch 로 생성 된 branch 확인
11. git checkout html -> html branch 로 옮겨라
12. git branch -> * 가 현재 branch 위치
13. html 파일 작성
14. git add index.html
15. git commit -> html 에 관한 commit
16. css 파일 작성
17. git add style.css
18. git commit -> css 에 관한 commit
19. git branch feature html -> html 하위  feature 생성
20. git branch -d branch이름 -> branch 삭제 명령어
21. feature, fix 에 각각 다르게 생성되어 있는 html 파일 html branch에 merge
22. git merge <해당 commit 번호>
23. git log --graph -> Terminal 에서 branch graph 로 확인




# 과제
* 버전관리란 무엇이고, 버전 관리 방법에는 어떤것들이 있는지
* git 명령어(command) 정리하기
* 위 두 가지는 오늘 날짜의 과제 제출 폴더에 Mark Down 문법으로 정리하기 