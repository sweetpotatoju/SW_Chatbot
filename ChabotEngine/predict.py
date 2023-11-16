import tensorflow as tf

from ChabotEngine.preprocess import preprocess_sentence

MAX_LENGTH = 40


def decoder_inference(sentence, start_token, end_token, tokenizer, model):
    sentence = preprocess_sentence(sentence)

    sentence = tf.expand_dims(
        start_token + tokenizer.encode(sentence) + end_token, axis=0)

    output_sequence = tf.expand_dims(start_token, 0)

    for i in range(MAX_LENGTH):
        predictions = model(inputs=[sentence, output_sequence], training=False)
        predictions = predictions[:, -1:, :]

        predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

        if tf.equal(predicted_id, end_token[0]):
            break

        output_sequence = tf.concat([output_sequence, predicted_id], axis=-1)

    return tf.squeeze(output_sequence, axis=0)


def sentence_generation(sentence, start_token, end_token, tokenizer, model):
    prediction = decoder_inference(sentence, start_token, end_token, tokenizer, model)

    predicted_sentence = tokenizer.decode(
        [i for i in prediction if i < tokenizer.vocab_size])

    print('입력 : {}'.format(sentence))
    print('출력 : {}'.format(predicted_sentence))

    return predicted_sentence


