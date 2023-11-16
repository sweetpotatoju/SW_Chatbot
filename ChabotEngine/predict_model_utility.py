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

while True:
    input_sentence = input("You: ")

    #여기서 원하는 답이 안나오면 팝업이나 이벤트를 띄우게 변경해도 괜찮을듯 함
    if input_sentence.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break

    response = sentence_generation(input_sentence, start_token, end_token, tokenizer, model)
    print(f"Chatbot: {response}")

