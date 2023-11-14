from ChabotEngine.SubwordTextEncoder import *
from Dataset_bot import *
from ChabotEngine.transforemer import *
from ChabotEngine.preprocess import *
from ChabotEngine.train import *

#기본 환경 설정
MAX_SAMPLES = 50000

BATCH_SIZE = 64
BUFFER_SIZE = 20000


print(MAX_SAMPLES)
print(MAX_LENGTH)
print("-----------------------------------------------------")

questions, answers = load_conversations(train_data['Q'], train_data['A'])
print('전체 샘플 수 :', len(questions))
print('전체 샘플 수 :', len(answers))
print("-----------------------------------------------------")

print('전처리 후의 22번째 질문 샘플: {}'.format(questions[21]))
print('전처리 후의 22번째 답변 샘플: {}'.format(answers[21]))
print("-----------------------------------------------------")

# build_and_tokenize_corpus 함수 사용
questions, answers, vocab_size = build_and_tokenize_corpus(questions, answers)
print('단어장의 크기 :', vocab_size)
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

VOCAB_SIZE = 8175

EPOCHS = 10
model = build_model(VOCAB_SIZE)
model.fit(dataset, epochs=EPOCHS, verbose=1)
def decoder_inference(sentence):
    sentence = preprocess_sentence(sentence)

    sentence = tf.expand_dims(
        START_TOKEN + tokenizer.encode(sentence) + END_TOKEN, axis=0)

    output_sequence = tf.expand_dims(START_TOKEN, 0)

    for i in range(MAX_LENGTH):
        predictions = model(inputs=[sentence, output_sequence], training=False)
        predictions = predictions[:, -1:, :]

        predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

        if tf.equal(predicted_id, END_TOKEN[0]):
            break

        output_sequence = tf.concat([output_sequence, predicted_id], axis=-1)

    return tf.squeeze(output_sequence, axis=0)

def sentence_generation(sentence):
    prediction = decoder_inference(sentence)

    predicted_sentence = tokenizer.decode(
        [i for i in prediction if i < tokenizer.vocab_size])

    print('입력 : {}'.format(sentence))
    print('출력 : {}'.format(predicted_sentence))

    return predicted_sentence

sentence_generation("가장 확실한 건 뭘까?")
