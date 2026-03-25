import sys
sys.path.insert(0, 'FlaskExample')
from db import Database

try:
    db = Database()
    cursor = db.connection.cursor()

    # 테이블 삭제
    print("테이블 삭제 중...")
    cursor.execute("DROP TABLE IF EXISTS bmi_records")
    db.connection.commit()
    print("테이블 삭제 완료")

    # UTF-8MB4 테이블 생성
    print("UTF-8MB4 테이블 생성 중...")
    sql = """
    CREATE TABLE bmi_records (
        id INT AUTO_INCREMENT PRIMARY KEY,
        weight FLOAT NOT NULL,
        height FLOAT NOT NULL,
        bmi FLOAT NOT NULL,
        category VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
    """
    cursor.execute(sql)
    db.connection.commit()
    print("UTF-8MB4 테이블 생성 완료!")

    # 확인
    cursor.execute("SHOW CREATE TABLE bmi_records")
    result = cursor.fetchone()
    print("\n테이블 구조:")
    print(result['Create Table'])
    
    db.close()
    print("\n완료!")
except Exception as e:
    print(f"에러 발생: {e}")
    import traceback
    traceback.print_exc()

db.close()
