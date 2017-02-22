from . import config as cfg
import random
import os
import codecs
from jakobmorrison.settings import BASE_DIR
import multiprocessing
import nltk
from gensim.models import word2vec as w2v
import sklearn.manifold
import pandas as pd
import re
import numpy as np

cfg = cfg.Config
book_path = os.path.join(BASE_DIR, 'books/static/books/book_list/')
trained_path = os.path.join(BASE_DIR, 'books/static/books/trained/')
vector_path = os.path.join(BASE_DIR, 'books/static/books/vector/')
nltk_path = os.path.join(BASE_DIR, 'books/static/books/nltk/')

class Book_Methods():
    def __init__(self):
        pass
    def clean_up(self,lookup):
        book_raw = u""
        book_file_name = os.path.join(book_path, lookup+".txt")
        with codecs.open(book_file_name, 'r', 'utf-8') as book_file:
            book_raw = book_raw + book_file.read()

        tokenizer = nltk.data.load(nltk_path+"/punkt/english.pickle")
        raw_sentences = tokenizer.tokenize(book_raw)

        sentences = []
        for raw_sentence in raw_sentences:
            if len(raw_sentence) > 0:
                clean = re.sub("[^a-zA-Z]", " ", raw_sentence)
                sentences.append(clean.split())

        if not os.path.exists(trained_path):
            os.makedirs(trained_path)
        if not os.path.exists(vector_path):
            os.makedirs(vector_path)

        if not os.path.exists(os.path.join(trained_path, lookup+".w2v")):
            self.build_w2v_model(sentences, lookup)
        if not os.path.exists(os.path.join(vector_path, lookup+".pkl")):
            self.create_2d_word_vectors(lookup)
        return sentences

    def build_w2v_model(self, sentences, lookup):
        # see jupyter notebook for description of variables.
        book2vec = w2v.Word2Vec(
            seed=1,
            workers=multiprocessing.cpu_count(),
            size=300,
            min_count=3,
            window=7,
            sample=1e3
        )
        book2vec.build_vocab(sentences)
        book2vec.train(sentences)
        book2vec.save(os.path.join(trained_path, lookup+".w2v"))

    def create_2d_word_vectors(self, lookup):
        tsne = sklearn.manifold.TSNE(n_components=2, random_state=0)
        book2vec = w2v.Word2Vec.load(os.path.join(trained_path, lookup+".w2v"))
        all_word_vectors_matrix = book2vec.syn0
        all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)
        points = pd.DataFrame(
            [
                (word, coords[0], coords[1])
                for word, coords in [
                    (word, all_word_vectors_matrix_2d[book2vec.vocab[word].index])
                    for word in book2vec.vocab
                    ]
                ],
            columns=["word", "x", "y"]
        )
        points.to_pickle(os.path.join(vector_path, lookup+".pkl"))

    def get_stats(self, sentences, lookup):
        word_count = sum([len(x) for x in sentences])
        sentence_count =  len(sentences)
        words_per_sentence = word_count/sentence_count

        book2vec = w2v.Word2Vec.load(os.path.join(trained_path, lookup+".w2v"))

        unique_words = len(book2vec.vocab)
        average_unique_word_length = sum([len(x) for x in list(book2vec.vocab.keys())]) / len(list(book2vec.vocab.keys()))
        unique_words_len_arr = np.array([len(key) for key in list(book2vec.vocab.keys())]) # for histogram
        vocab_density = float("%.2f"%(word_count/unique_words))

        # for word cloud
        # occurance_arr_1 = np.array([book2vec.vocab.get(key).count for key in list(book2vec.vocab.keys()) if len(key) <= 4])  # for histogram
        # std_1 = occurance_arr_1.mean() + occurance_arr_1.std() * 3
        occurance_arr_2 = np.array([book2vec.vocab.get(key).count for key in list(book2vec.vocab.keys()) if len(key) > 4 and len(key) <= 8])  # for histogram
        std_2 = occurance_arr_2.mean() + occurance_arr_2.std() * 2.5
        occurance_arr_3 = np.array([book2vec.vocab.get(key).count for key in list(book2vec.vocab.keys()) if len(key) > 9 and len(key)<=13])
        std_3 = occurance_arr_3.mean() + occurance_arr_3.std() * 2.5
        occurance_arr_4 = np.array([book2vec.vocab.get(key).count for key in list(book2vec.vocab.keys()) if len(key) > 13])
        std_4 = occurance_arr_4.mean() + occurance_arr_4.std() * 1.5


        # dict_1 = [{key: book2vec.vocab.get(key).count} for key in list(book2vec.vocab.keys()) if book2vec.vocab.get(key).count > std_1 and len(key) <= 4]
        dict_2 = [{key: book2vec.vocab.get(key).count} for key in list(book2vec.vocab.keys()) if book2vec.vocab.get(key).count > std_2 and len(key) > 4 and len(key)<=8]
        dict_3 = [{key: book2vec.vocab.get(key).count} for key in list(book2vec.vocab.keys()) if book2vec.vocab.get(key).count > std_3 and len(key) > 9 and len(key)<=13]
        dict_4 = [{key: book2vec.vocab.get(key).count} for key in list(book2vec.vocab.keys()) if book2vec.vocab.get(key).count > std_4 and len(key) > 13]

        occurance_dict =  dict_2 + dict_3 + dict_4

        # replace dict item with a similar word.

        # random.shuffle(occurance_dict)
        # remove_key = []
        # new_dict = {}
        # for x in range(0, random.randrange(1, len(occurance_dict))):
        #     key = (list(occurance_dict[x].items())[0][0])
        #     print(book2vec.most_similar(key)[0][0])

        context = {
            "word_count":word_count,
            "sentence_count":sentence_count,
            "words_per_sentence":words_per_sentence,
            "unique_words":unique_words,
            "average_unique_word_length":average_unique_word_length,
            "unique_words_len_arr":unique_words_len_arr,
            "vocab_density":vocab_density,
            "occurance_dict":occurance_dict
        }
        return context


    def word_cloud(words):
        x, y = zip(*words)
        max_val = int((sum(list(y)) / float(len(list(y)))))
        random.shuffle(words)
        word_cloud = dict(words)
        new_word_list = []
        less_than = 0
        greater_than = 0
        middle = 0
        for key,val in word_cloud.items():
            if (len(key) >= 12 and val>=max_val and greater_than<=20):
                new_word_list.append({'text': key, 'weight': val})
                greater_than += 1
            elif (len(key) >= 9 and len(key) <12 and val>=max_val and middle<=20):
                new_word_list.append({'text': key, 'weight': val})
                middle += 1
            elif (len(key) >=6 and len(key) <9 and val>=max_val and less_than<=20):
                new_word_list.append({'text': key, 'weight': val})
                less_than += 1

        return new_word_list

    def calculate_regresssion(x,y,max):
        a = ( sum(y) * sum([float(i)*float(i) for i in x]) - sum(x) * sum([a*b for a,b in zip(x,y)]) )/( len(x)*sum([float(i)*float(i) for i in x]) - sum(x)*sum(x) )
        b = ( len(x)*sum([a*b for a,b in zip(x,y)]) - sum(x)*sum(y) )/( len(x)*sum([float(i)*float(i) for i in x]) - sum(x)*sum(x) )
        xl = 0
        xh = max+5000
        yl = a + b*xl
        yh = a + b*xh
        return [[xl, yl], [xh, yh]]
