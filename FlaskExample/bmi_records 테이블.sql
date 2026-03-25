USE test;  

-- 데이터베이스를 UTF8MB4로 설정
ALTER DATABASE test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 기존 테이블 삭제
DROP TABLE IF EXISTS bmi_records;

-- 테이블 생성 (UTF-8MB4 명시)
CREATE TABLE bmi_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    weight FLOAT NOT NULL,
    height FLOAT NOT NULL,
    bmi FLOAT NOT NULL,
    category VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;