
from sentence_transformers import SentenceTransformer, util
import random

class Quote:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, "r") as input_file:
            self.quotes = input_file.readlines()
    

    def get(self):
        print('🥠 {}'.format(random.choice(self.quotes)))


    def add(self, new_quote):

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        embedding_newquote= model.encode(new_quote, convert_to_tensor=True)
        
        similar_quotes = []
        for existing_quote in self.quotes:
            embedding_existing_quote = model.encode(existing_quote, convert_to_tensor=True)
            similartity = util.pytorch_cos_sim(embedding_newquote, embedding_existing_quote).item()
            if similartity > 0.9:
                similar_quotes.append(existing_quote)

        if similar_quotes:
            print('Similar quotes already exist: \n')
            for quote in similar_quotes:
                print(f'🥠 {quote}')
            return
        
        with open(self.file_path, "a") as output_file:
            output_file.write(new_quote + '\n')
            print('Quote added successfully!')