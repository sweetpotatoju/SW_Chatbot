import urllib
import pandas as pd
from urllib.request import urlopen


urllib.request.urlretrieve("https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv", filename="ChatBotData.csv")
train_data = pd.read_csv('ChatBotData.csv')
train_data.head()

print('챗봇 샘플의 개수 :', len(train_data))
print(train_data.isnull().sum())
