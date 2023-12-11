# chatbot/chatbot_logic.py
from django.http import JsonResponse
import pickle
from ChabotEngine.predict import *
from ChabotEngine.train import *
from ChabotEngine.transforemer import *
from tensorflow import keras
import os

from chatbotAdmin.models import QATable
from main.models import Question

# 현재 스크립트의 디렉토리
script_dir = os.path.dirname(os.path.abspath(__file__))

# ChabotEngine 디렉토리로 이동한 후 파일 경로 지정
model_path = os.path.join(script_dir, '..', 'ChabotEngine', 'saved_transformer_model')
token_path = os.path.join(script_dir, '..', 'ChabotEngine', '토큰_및_토크나이저.pkl')

# 필요한 데이터 및 모델 로드
with open(token_path, 'rb') as file:
    loaded_data = pickle.load(file)

start_token = loaded_data['start_token']
end_token = loaded_data['end_token']
tokenizer = loaded_data['tokenizer']

custom_objects = {
    'PositionalEncoding': PositionalEncoding,
    'MultiHeadAttention': MYMultiHeadAttention,
    'CustomSchedule': CustomSchedule,
    'loss_function': loss_function
}

model = keras.models.load_model(model_path, custom_objects=custom_objects)


#
# def get_alternative_response(user_input):
#     # "질문등록"이라는 특정 문자열이 포함되어 있으면 질문 등록 로직을 실행합니다.
#     if "질문등록" in user_input:
#         # 예시로 간단한 비밀번호 확인 로직
#         password = input("비밀번호를 입력하세요(4자리 숫자): ")
#
#         # 실제 사용시는 보안을 강화해야 합니다. (예: 해시 및 안전한 인증 방법 사용)
#         if len(password) == 4:
#             question_text = input("질문을 입력하세요: ")
#
#             # Question 객체를 생성하여 데이터베이스에 저장
#             question = Question(question_text=question_text, password=password)
#             question.save()
#
#             alternative_response = "질문이 등록되었습니다."
#         else:
#             alternative_response = "비밀번호는 4자 이하여야 합니다."
#
#     elif "질문확인" in user_input:
#
#         count = Question.objects.filter(answer_status='N').count()
#
#         alternative_response = f"현재 등록된 답변이 필요한 질문 수: {count}"
#     else:
#         # 다른 경우에는 기본적으로 대체 응답을 생성합니다.
#         alternative_response = "대체 응답입니다."
#
#     return alternative_response
#
#
# def get_chatbot_response(user_input):
#     # user_input에서 특정 조건을 확인합니다.
#     if "질문등록" in user_input:
#         # 대체 로직을 실행합니다.
#         response = get_alternative_response(user_input)
#     else:
#         # 기존 챗봇 로직을 계속 진행합니다.
#         response = sentence_generation(user_input, start_token, end_token, tokenizer, model)
#
#     return response

def check_question_answer_status(password_input):
    try:
        # 비밀번호에 해당하는 질문 가져오기
        question = Question.objects.get(password=password_input)

        try:
            # 질문에 대한 답변이 있는 경우 해당 답변 가져오기
            qa_table = QATable.objects.get(q=question)
            answer = qa_table.a

            return f"질문: {question.question_text}\n답변: {answer}"

        except QATable.DoesNotExist:
            # 질문에 대한 답변이 아직 없는 경우
            return "아직 답변이 완료되지 않았습니다."

    except Question.DoesNotExist:
        # 해당 비밀번호로 등록된 질문이 없는 경우
        return "등록된 질문이 없습니다."


def get_alternative_response(user_input):
    if "질문등록하기" in user_input:
        return "비밀번호와 질문을 입력하세요. (ex.질문 등록: 1234, 질문)"

    elif "질문확인" in user_input:
        return "비밀번호를 입력하세요. (ex.비밀번호: 1234)"

    elif "비밀번호" in user_input:
        password_input = user_input.replace("비밀번호:", "").strip()

        if len(password_input) == 4:
            return check_question_answer_status(password_input)
        else:
            return "비밀번호는 4자 이하여야 합니다."



    elif "질문등록" in user_input:
        input_str = user_input.replace("질문등록:", "")
        password_input, question_input = map(str.strip, input_str.split(','))

        if len(password_input) == 4:
            # Question 객체를 생성하여 데이터베이스에 저장
            question = Question(question_text=question_input, password=password_input)
            question.save()

            return "질문이 등록되었습니다."
        else:
            return "비밀번호는 4자 이하여야 합니다."
    else:
        return "대체 응답입니다."


def get_chatbot_response(user_input):
    if "질문등록하기" in user_input or "질문등록" in user_input or "질문확인" in user_input or "비밀번호" in user_input:
        response = get_alternative_response(user_input)
    else:
        # 기존 챗봇 로직을 계속 진행합니다.
        response = sentence_generation(user_input, start_token, end_token, tokenizer, model)

    return response
