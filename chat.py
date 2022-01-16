import random
import json

import torch

from chatbot_meaning_finder import NeuralNet
from chatbot_functions import sack_of_words, tokenize
from chat_app_scenario_page import scene_num

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

intents_name = f'intents{scene_num}.json'

with open(intents_name, 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Lang-Bot"


def get_response(msg):
    sentence = tokenize(msg)
    X = sack_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.6:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "I do not understand.."