import mysql.connector
from mysql.connector import Error
import pandas as pd

# MySQL 서버 연결 설정
db_config = {
    'user': 'test1',
    'password': 'data3wh!!',
    'host': '210.117.175.207',
    'port': 6130,
    'database': 'chatbot',
    'charset': 'utf8mb4',
}

# MySQL에 연결
connection = None
try:
    connection = mysql.connector.connect(**db_config)

    # 데이터베이스 연결을 기반으로 한 MySQL 쿼리 실행을 위한 커서 생성
    cursor = connection.cursor()

    # sample 테이블이 이미 존재하는지 확인하고, 없으면 생성
    create_table_query = """
    CREATE TABLE IF NOT EXISTS sample (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Question VARCHAR(255),
        Answer VARCHAR(255),
        Label INT
    )
    """
    cursor.execute(create_table_query)

    # 데이터를 MySQL 테이블에 삽입
    data_to_insert = [
      #  ("집!", "가세요.", 0),
    ]

    for data in data_to_insert:
        insert_data_query = """
        INSERT INTO sample (Question, Answer, Label) VALUES (%s, %s, %s)
        """
        cursor.execute(insert_data_query, data)

    connection.commit()

    # 특정 id에 해당하는 행 삭제 -> 사용하지 않을땐 4줄 주석처리, ID는 고유번호
    # id_to_delete = 7328
    # delete_query = "DELETE FROM sample WHERE id = %s"
    # cursor.execute(delete_query, (id_to_delete,))
    # connection.commit()

    # 특정 id에 해당하는 Answer 수정 -> 사용하지 않을땐 주석처리, ID는 고유번호
    # id_to_update = 7329
    # new_answer = "집에 가도 될까?"
    # update_query = "UPDATE sample SET Question = %s WHERE id = %s"
    # cursor.execute(update_query, (new_answer, id_to_update))
    # connection.commit()

    # sample 테이블에서 데이터 가져오기
    query = "SELECT * FROM sample"
    cursor.execute(query)

    # 결과를 데이터프레임으로 변환
    columns = [desc[0] for desc in cursor.description]
    sample_data = pd.DataFrame(cursor.fetchall(), columns=columns)

    # 결과 출력
    print("-----------------------------------------------")
    print('챗봇 샘플의 개수:', len(sample_data))
    print(sample_data.isnull().sum())
    print(sample_data)

except Error as e:
    print(f"Error: {e}")

finally:
    # 연결 종료
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
