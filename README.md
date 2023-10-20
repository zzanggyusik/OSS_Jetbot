# OSS_Jetbot



## OSS 프로젝트 실습 및 개발을 위한 README.MD

### 본 레포지토리는 한밭대학교 인공지능소프트웨어 학과에서 진행되는 OSS 프로젝스 실습 및 개발을 위해 제작됨

### 프로젝트 참여자는 해당 내용을 숙지하여 프로젝트를 진행하도록 한다(주의사항 숙지 필수).

### 프로젝트 개발환경을 위한 사전 설정

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

### 프로젝트 실습 준비

1. PC에서 https://github.com/zzanggyusik/OSS_Jetbot 에 들어가 Fork 버튼을 누른다.
2. Fork하여 자신의 계정을 소유로 한 Repo를 생성한다. 이때, OSS_Jetbot + _(팀명 혹은 번호) 로 한다. 예시 OSS_Jetbot_Team5
   <br>
   한국어는 안됨
3. Jetson Nano의 전원을 켜고 터미널을 이용하여 포크하여 만든 Git hub repository를 clone 한다.

### Jetson Nano 원격 실습 준비

1. Jetson Nano의 네트워크를 확인한다(Wifi IP 번호 확인 : xxx.xxx.xxx.xxx)
2. PC에서 http://(확인한 IP):8888 을 이용하여 Jupyter 노트북에 접속한다(기본 세팅)
3. 비밀번호는 yahboom 으로 Jetbot의 비밀번호와 동일함
4. Jupyter 노트북에 파일 탐색기를 활용하여 자신이 clone한 디렉토리에 접근 후 프로젝트 진행

### 프로젝트 실습 및 개발 방법

1. git flow init 후 엔터
2. git flow feature start {feature 브랜치 이름}
3. git checkout feature/{방금 생성한 브랜치 이름}
4. 프로젝트 개발 완료후
   - git add .

   - git commit -m "{message}"

   - git push origin feature/{생성한 브랜치 이름}
     <br>이떄 아래 그림과 유사한 error 메세지가 뜬다면
     <br>![스크린샷 2022-12-14 오후 8 22 39](https://user-images.githubusercontent.com/97441976/207582588-b1d701dc-798f-49ac-a9bd-2a481597d091.png)
     <br> 중간의 git push --set 으로 시작하는 라인을 복사해서 다시 입력
5. 브랜치 통합
   예: 000님 기능 구현하신 브랜치 디벨롭에 올려주세요.
   - git checkout develop
   - git pull
   - git merge feature/{생성한 이름} -m "{message}"
   - git commit -m "{message}"
   - git push

### 주의 사항

1. 깃허브의 기본은 main으로 설정되어 있다. 따라서 개발을 진행할때 본인의 위치가 main이 아닌 개인 feature(진행중인 프로젝트 브랜치)로 설정되어 있는지 반드시 확인해야 한다.
2. 깃허브의 메인은 되도록 건드리지 않는다.
   이는 개인 feature를 이용하여 개발을 진행하여 디벨롭 브랜치를 이용하여 통합을 확인한다.
3. 본인 feature이외 다른 프로젝트 참여자의 feature는 되도록 건드리지 않는다.
4. 충돌 방지를 위해 다른 사람이 작성한 내용은 수정하지 않는다.
5. 깃허브 사용중 충돌 발생및 기타 오류 발생시 조교에게 물어볼 것



작성자 : SysAI Lab 함규식

Email: gsham@edu.hanbat.ac.kr

Phone: 010-9946-9297

K-talk: zzanggyusik



Contributer : SysAI Lab 김현기
