# OSS_Jetbot



## OSS 프로젝트 실습 및 개발을 위한 README.MD

### 본 레포지토리는 한밭대학교 인공지능소프트웨어 학과에서 진행되는 OSS 프로젝스 실습 및 개발을 위해 제작됨

### 프로젝트 참여자는 해당 내용을 숙지하여 프로젝트를 진행하도록 한다(주의사항 숙지 필수).

### 프로젝트 개발환경을 위한 사전 설정

- VScode 설치
- Github 아이디 필요

### Github

- 깃허브 사용 목적 :
  1. 코드 분할 개발 후 통합 과정에서 빈번한 오류 발생
     이를 해결 하기 위해 통합 환경을 구축 후 개발 진행
  2. 또한 깃허브는 이번 버전또한 저장하고 있어 오류 발생 및 데이터가 삭제되었을시 빠른 복구가 가능
- 기본 용어 정리 :
  - 레포지토리 : 저장장소(repo)
  - git init : 초기화
  - git clone : GitHub에 있는 저장소의 주소를 입력하여 로컬로 복제
  - 브랜치 : 자신만의 버전
  - 커밋 : 코드를 변경한 후 스냅샷을 찍음. -m 을 이용하여 메세지를 남김
  - git commit -m "{message}" : 커밋 명령어
  - git checkout {원하는 브랜치} : 원하는 브랜치로 이동
  - git push : 작업하는 로컬환경(본인 컴퓨터)에서 깃허브 프로젝트 레포지리에 올릴때 사용
  - git pull : 레포지토리에 있는 최신 버전을 받아올때 사용
  - git merge {합칠 브랜치} -m "{message}" : 현재 브랜치에서 다른 브랜치를 합칠때 사용

### 프로젝트 실습 및 개발 방법

1. VSCode를 실행하고 GitHub repository를 clone 한다.
   ![스크린샷 2022-12-14 오후 8 02 53](https://user-images.githubusercontent.com/97441976/207578304-275e9d38-1b8f-4859-a15a-229c6b5e2b23.png)

2. 아래 그림과 같은 창에 레포지토리의 주소를 입력한다.
   <br>
   ![스크린샷 2022-12-14 오후 8 03 43](https://user-images.githubusercontent.com/97441976/207578636-c618f715-2db9-42d7-b2bd-2aa599c506d9.png)
   <br>
   (본 프로젝트의 경우 https://github.com/zzanggyusik/OSS_Jetbot.git)

3. Sublinemerge를 이용하여 레포지토리 열기.

   - Local Repositories의 Open Repository
     폴더는 1, 2 번을 진행하며 clone으로 만들어진 폴더 선택

4. VSCode에서 터미널 실행 (!!아래 명령어는 각 오류가 없을시 다음단계 진행!!)
   <br>
   개발 브랜치까지 가는 방법 :

   - git pull

   - git checkout develop

   - git pull
   - git flow feature start {본인 이름 또는 팀}

   Sublimemerge를 이용하여 현재 위치 확인
   <br>![스크린샷 2022-12-14 오후 8 18 20](https://user-images.githubusercontent.com/97441976/207581727-c0fdfb88-aa26-4f14-99ed-986ccf608db1.png)
   <br>
   이처럼 feature/ 로 시작하는 곳에 불이 들어와있어야 함

5. 왼쪽 Explorer(종이 두장 이모티콘)를 이용하여 개발 진행

6. 개발 완료후

   - git add .

   - git commit -m "{message}"

   - git push
     <br>이떄 아래 그림
     <br>![스크린샷 2022-12-14 오후 8 22 39](https://user-images.githubusercontent.com/97441976/207582588-b1d701dc-798f-49ac-a9bd-2a481597d091.png)
     <br>과 같은 메세지가 뜨는데 중간의 git push --set 으로 시작하는 라인을 복사해서 다시 입력

7. 브랜치 통합
   예: 000님 기능 구현하신 브랜치 디벨롭에 올려주세요.

   - git checkout develop
   - git pull
   - git merge feature/{생성한 이름} -m "{message}"
   - git commit -m "{message}"
   - git push

### 주의 사항

1. 깃허브의 기본은 main으로 설정되어 있다. 따라서 개발을 진행할때 본인의 위치가 main이 아닌 개인 feature로 설정되어 있는지 반드시 확인해야 한다.
2. 깃허브의 메인은 되도록 건드리지 않는다.
   이는 개인 feature를 이용하여 개발을 진행하여 디벨롭 브랜치를 이용하여 통합을 확인한다.
3. 본인 feature이외 다른 프로젝트 참여자의 feature는 되도록 건드리지 않는다.
4. 충돌 방지를 위해 다른 사람이 작성한 내용은 수정하지 않는다.
5. 깃허브 사용중 충돌 발생및 기타 오류 발생시 프로젝트 관리자에게 물어본다.



작성자 : SysAI Lab 함규식
Contributer : SysAI Lab 김현기