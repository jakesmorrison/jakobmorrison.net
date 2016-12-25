from . import config as cfg
from collections import Counter
import random

cfg = cfg.Config

class Book_Methods():
    def clean_up(book_file):
        book_string = ""
        for line in book_file:
            line = line.lower()
            line = line.replace("\n", " ")
            line = line.replace(".", " ")
            line = line.replace("?", " ")
            line = line.replace("!", " ")
            line = line.replace(";", " ")
            line = line.replace(":", " ")
            line = line.replace("\"", " ")
            line = line.replace("\'", " ")
            line = line.replace(",", " ")
            line = line.replace("-", " ")
            line = line.replace("—", " ")
            line = line.replace("(", " ")
            line = line.replace(")", " ")
            line = line.replace("[", " ")
            line = line.replace("]", " ")
            line = line.replace("‘", " ")
            line = line.replace("“", " ")
            line = line.replace("’", " ")
            line = line.replace("chapter", " ")
            line = line.replace("Chapter", " ")
            for x in list(range(0, 10)): line = line.replace(str(x), " ")
            book_string = book_string + "" + line
        book_string = ' '.join(book_string.split())
        return book_string

    def get_stats(book_string):
        words = book_string.split(" ")
        unique_words = set(words)
        long_words = [x for x in unique_words if len(x)>=8]
        vocab_density = len(words)/len(unique_words)
        # print(len(words))
        # print(len(unique_words))
        # print(len(long_words))
        return words, unique_words, vocab_density


    def word_cloud(words):
        temp = []
        for w in words:
            if len(w) >= 6:
                temp.append(w)

        word_cloud = Counter(temp)
        word_cloud = sorted(word_cloud.items())
        word_cloud = random.sample(word_cloud, len(word_cloud))
        word_cloud = dict(word_cloud)

        new_word_list = []
        less_than = 0
        greater_than = 0
        for key,val in word_cloud.items():
            if (len(key) > 10 and val>=10 and greater_than<=20):
                new_word_list.append({'text': key, 'weight': val})
                greater_than += 1
            if (len(key) <= 10 and val>=10 and less_than<=20):
                new_word_list.append({'text': key, 'weight': val})
                less_than += 1

        # print(sorted(word_cloud.items()))
        return new_word_list

    def calculate_regresssion(x,y,max):
        a = ( sum(y) * sum([float(i)*float(i) for i in x]) - sum(x) * sum([a*b for a,b in zip(x,y)]) )/( len(x)*sum([float(i)*float(i) for i in x]) - sum(x)*sum(x) )
        b = ( len(x)*sum([a*b for a,b in zip(x,y)]) - sum(x)*sum(y) )/( len(x)*sum([float(i)*float(i) for i in x]) - sum(x)*sum(x) )
        xl = 0
        xh = max+5000
        yl = a + b*xl
        yh = a + b*xh
        return [[xl, yl], [xh, yh]]