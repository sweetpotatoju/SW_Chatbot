import os

import tensorflow as tf
import tensorflow_datasets as tfds


def build_and_tokenize_corpus(questions, answers, max_length=40, target_vocab_size=2 ** 13):

    tokenizer = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            questions + answers, target_vocab_size=target_vocab_size)
    print(tokenizer)

    START_TOKEN, END_TOKEN = [tokenizer.vocab_size], [tokenizer.vocab_size + 1]
    VOCAB_SIZE = tokenizer.vocab_size + 2

    print('START_TOKEN의 번호 :', [tokenizer.vocab_size])
    print('END_TOKEN의 번호 :', [tokenizer.vocab_size + 1])

    print('정수 인코딩 후의 21번째 질문 샘플: {}'.format(tokenizer.encode(questions[21])))
    print('정수 인코딩 후의 21번째 답변 샘플: {}'.format(tokenizer.encode(answers[21])))
    print("-----------------------------------------------------")

    def tokenize_and_filter(inputs, outputs):
        tokenized_inputs, tokenized_outputs = [], []

        for (sentence1, sentence2) in zip(inputs, outputs):
            sentence1 = START_TOKEN + tokenizer.encode(sentence1) + END_TOKEN
            sentence2 = START_TOKEN + tokenizer.encode(sentence2) + END_TOKEN

            if len(sentence1) <= max_length and len(sentence2) <= max_length:
                tokenized_inputs.append(sentence1)
                tokenized_outputs.append(sentence2)

        tokenized_inputs = tf.keras.preprocessing.sequence.pad_sequences(
            tokenized_inputs, maxlen=max_length, padding='post')
        tokenized_outputs = tf.keras.preprocessing.sequence.pad_sequences(
            tokenized_outputs, maxlen=max_length, padding='post')

        return tokenized_inputs, tokenized_outputs

    questions, answers = tokenize_and_filter(questions, answers)
    print('질문 데이터의 크기(shape) :', questions.shape)
    print('답변 데이터의 크기(shape) :', answers.shape)
    print(questions[0])
    print(answers[0])

    return questions, answers, VOCAB_SIZE, START_TOKEN, END_TOKEN, tokenizer


