#web_app/services/basilica.py

import basilica
import os
from dotenv import load_dotenv


load_dotenv() #parse the .env file for environment variables

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))#<basilica.Connection object at 0x000002AAACDB3FC8>

if if __name__ == "__main__":
    
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]