import pickle

from tensorflow import keras

from ChabotEngine.predict import sentence_generation
from ChabotEngine.transforemer import *
from ChabotEngine.train import *

custom_objects = {
    'PositionalEncoding': PositionalEncoding,
    'MultiHeadAttention': MYMultiHeadAttention,
    'CustomSchedule': CustomSchedule,
    'loss_function': loss_function
}


model = keras.models.load_model('saved_transformer_model', custom_objects=custom_objects)

with open("토큰_및_토크나이저.pkl", 'rb') as file:
    loaded_data = pickle.load(file)

start_token = loaded_data['start_token']
end_token = loaded_data['end_token']
tokenizer = loaded_data['tokenizer']

input_sentence = ("영화 보러 갈까?")
sentence_generation(input_sentence, start_token, end_token, tokenizer, model)


