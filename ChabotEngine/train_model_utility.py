from ChabotEngine.SubwordTextEncoder import *
from Dataset_bot import *
from ChabotEngine.preprocess import *
from ChabotEngine.train import *
from ChabotEngine.predict import *
import pickle

# 기본 환경 설정
MAX_SAMPLES = 50000
BATCH_SIZE = 64
BUFFER_SIZE = 20000

print(MAX_SAMPLES)
print("-----------------------------------------------------")

questions, answers = load_conversations(train_data['Question'], train_data['Answer'])
print('전체 샘플 수 :', len(questions))
print('전체 샘플 수 :', len(answers))
print("-----------------------------------------------------")

print('전처리 후의 22번째 질문 샘플: {}'.format(questions[13]))
print('전처리 후의 22번째 답변 샘플: {}'.format(answers[13]))
print("-----------------------------------------------------")

# build_and_tokenize_corpus 함수 사용
questions, answers, vocab_size_, start_token, end_token, tokenizer_ = build_and_tokenize_corpus(questions, answers)

print('단어장의 크기 :', vocab_size_)
print('필터링 후의 샘플 개수: {}'.format(len(questions)))
print('필터링 후의 샘플 개수: {}'.format(len(answers)))

dataset = tf.data.Dataset.from_tensor_slices((
    {
        'inputs': questions,
        'dec_inputs': answers[:, :-1]
    },
    {
        'outputs': answers[:, 1:]
    },
))

dataset = dataset.cache()
dataset = dataset.shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE)
dataset = dataset.prefetch(tf.data.experimental.AUTOTUNE)

VOCAB_SIZE = vocab_size_
EPOCHS = 100 # 훈련 횟수 설정
NUM_LAYERS = 6  # 인코더와 디코더의 층의 개수
D_MODEL = 512  # 인코더와 디코더 내부의 입, 출력의 고정 차원
NUM_HEADS = 8  # 멀티 헤드 어텐션에서의 헤드 수
UNITS = 512  # 피드 포워드 신경망의 은닉층의 크기
DROPOUT = 0.1  # 드롭아웃의 비율

model = build_model(VOCAB_SIZE, NUM_LAYERS, D_MODEL, NUM_HEADS, UNITS, DROPOUT, dataset, EPOCHS)
model.save("saved_transformer_model", save_format='tf')

with open("토큰_및_토크나이저.pkl", 'wb') as file:
    pickle.dump({
        'start_token': start_token,
        'end_token': end_token,
        'tokenizer': tokenizer_
    }, file)

