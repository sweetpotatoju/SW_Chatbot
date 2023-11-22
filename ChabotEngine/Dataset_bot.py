import mysql.connector
from mysql.connector import Error
import pandas as pd
from mysetting import *

# MySQL 서버 연결 설정

# MySQL에 연결
connection = None
try:
    connection = mysql.connector.connect(**db_config)

    # 데이터베이스 연결을 기반으로 한 MySQL 쿼리 실행을 위한 커서 생성
    cursor = connection.cursor()

    # chatbotadmin_qatable 테이블과 main_question 테이블을 조인하여 데이터 가져오기
    query = """
            SELECT chatbotadmin_qatable.*, main_question.question_text
            FROM chatbotadmin_qatable
            JOIN main_question ON chatbotadmin_qatable.q_id = main_question.id
        """
    cursor.execute(query)

    # 결과를 데이터프레임으로 변환
    columns = [desc[0] for desc in cursor.description]
    train_data = pd.DataFrame(cursor.fetchall(), columns=columns)

    # 결과 출력
    print("-----------------------------------------------")
    print('챗봇 샘플의 개수:', len(train_data))
    print(train_data.isnull().sum())
    print(train_data[['question_text', 'a', 'label']])

except Error as e:
    print(f"Error: {e}")

finally:
    # 연결 종료
    if connection and connection.is_connected():
        cursor.close()
        connection.close()

