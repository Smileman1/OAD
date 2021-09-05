# OAE
<img width="400" alt="OAE_Logo" src="https://user-images.githubusercontent.com/71224672/132128133-dd9c9049-6bd5-4436-81a0-88f021051b87.png" alt="image-20210830221721743" style="zoom:50%;">
유저들이 여러 사이트를 돌며 확인해야 하는 각 분야 랭킹을 한곳에 모아서 보여주는 서비스입니다.<br><br>
개인 프로젝트로 진행하였으며, 지정된 주소로 접속하면 PC, Mobile 모두 접속 가능하도록 개발하였습니다. 랭킹 정보를 가지고 오는 부분은 파이썬의 Beautifulsoup를 통하여 크롤링 하였고, 크롤링 한 데이터를 pymongo를 이용해 MongoDB에 저장하였습니다. 현재 영화, 주식, 음악 총 3개의 순위를 확인할 수 있으며 필요에 따라 바로 새로운 분야를 추가할 수 있도록 설계하였습니다. 추가로 업데이트 버튼을 통해 사용자가 원할 때 새로운 데이터를 받아올 수 있도록 편의성 기능을 추가하였습니다.

## 🥇 프로젝트 사용 기술
- [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)
- [Python](https://www.python.org/downloads/)
- [HTML](https://developer.mozilla.org/ko/docs/Web/HTML)
- [Notion](https://notion.so)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Robo 3T](https://robomongo.org/download)
- [PyCharm](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)


## 🥇 프로젝트 포커스
- 반복적인 작업은 공용 함수를 만들어 사용하여 개발의 효율을 높이기 위해 노력하였습니다.<br>
- 크롤링을 받아오는 데이터를 이해하고 필요한 부분만 받아오기 위해 노력하였습니다.<br>
- 어떠한 기술을 사용할 때는 그 기술이 사용하는 이유에 대하여 이해하고 사용하였습니다.<br>
- 데이터베이스에 저장된 값을 업데이트할 때 업데이트하는 값이 검증된 값인지 확인하기 위해 노력하였습니다.<br>
- 데이터베이스 접근을 최소화하도록 노력하였습니다.<br>

## 🥇 화면 구성도
<img width="500" alt="OAE_Logo" src="https://user-images.githubusercontent.com/71224672/132134116-e876f086-1915-49e1-bef8-5fdf50093f4a.png" alt="image-20210830221721743" style="zoom:50%;">

## 🥇 프로젝트 버전
- [OAE v1.0.0] : 프로젝트 생성
- [OAE v1.0.1] : 프로젝트 - MongoDB 연결 확인
- [OAE v1.0.2] : 영화 랭킹 db.insert, 화면 표시
- [OAE v1.0.3] : 코스피 랭킹, db.insert, 화면 표시
- [OAE v1.0.4] : 파일 병합
- [OAE v1.0.5] : 데이터 받아오기 및 데이터 업데이트 버 추가


## 🥇 시작하기
### Prerequisites
- pip
>```
>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
>```

### Installation
1. Install [mongoDB](https://www.mongodb.com/)
2. Clone the repo
>```
>git clone https://github.com/Smileman1/OAE.git
>```
3. Install PIP packages
>```
>pip install
>```
4. Start
>```
>python3 application.py
>```




## :phone: 연락처
Name - 김덕중<br>
email - ejrwnd1103@naver.com
