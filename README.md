# Flask BMI Calculator

Flask를 사용한 BMI(Body Mass Index) 계산 웹 애플리케이션입니다.

## 기능

- 체중과 신장을 입력하면 BMI 값과 체형 분류를 계산
- 계산된 데이터를 MariaDB에 저장
- 계산 이력 조회 기능

## 설치 및 실행

### 필수 요구사항
- Python 3.x
- MariaDB (또는 MySQL)
- pip

### 패키지 설치

```bash
pip install -r requirements.txt
```

### 데이터베이스 설정

1. MariaDB에 `test` 데이터베이스 생성
2. `bmi_records 테이블.sql` 파일 실행:

```bash
mysql -u root -p test < "bmi_records 테이블.sql"
```

### 애플리케이션 실행

```bash
python app.py
```

웹 브라우저에서 `http://127.0.0.1:5000` 접속

## 프로젝트 구조

```
.
├── app.py                      # Flask 메인 애플리케이션
├── bmi.py                      # BMI 계산 로직
├── db.py                       # 데이터베이스 연결 및 관리
├── requirements.txt            # Python 패키지 의존성
├── bmi_records 테이블.sql     # 데이터베이스 스키마
├── static/                     # CSS 파일
│   └── style.css
└── templates/                  # HTML 템플릿
    ├── index.html
    ├── result.html
    └── history.html
```

## 주요 파일 설명

- **app.py**: Flask 애플리케이션의 라우터 및 핸들러
- **bmi.py**: BMI 계산 클래스 (BMICalculator)
- **db.py**: MariaDB 데이터베이스 연결 및 데이터 저장/조회 (Database 클래스)
- **templates/**: 사용자 인터페이스 HTML 파일
- **static/**: CSS 스타일시트

## 사용법

1. 메인 페이지에서 체중(kg)과 신장(cm)입력
2. "계산" 버튼 클릭
3. BMI 결과 및 체형 분류 확인
4. History 페이지에서 과거 계산 이력 조회

## 기술 스택

- **Backend**: Python, Flask
- **Database**: MariaDB
- **Frontend**: HTML, CSS
- **Driver**: PyMySQL

## License

MIT License
