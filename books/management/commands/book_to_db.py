__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import Books
from .. import methods
import pandas as pd
import numpy as np
import json
from collections import Counter
import os
from jakobmorrison.settings import BASE_DIR
book_path = os.path.join(BASE_DIR, 'books/static/books/book_list/')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('title')
        parser.add_argument('author')
        parser.add_argument('lookup')
        parser.add_argument('type')
        parser.add_argument('genre')
        parser.add_argument('ds')
        parser.add_argument('df')

    def handle(self, *args, **options):
        self.book_to_db(options['title'],options['author'],options['lookup'],options['type'],options['genre'],options['ds'],options['df'])

    def book_to_db(self, title, author, lookup, type, genre, ds, df):
        book_string = methods.Book_Methods.clean_up(book_path+lookup)
        words, unique_words, vocab_density = methods.Book_Methods.get_stats(book_string)

        word_dict = []
        for w in words:
            word_dict.append(w)
        word_dict = Counter(word_dict)
        word_dict = json.dumps(list(sorted(word_dict.items())))

        s = Books(
            Title=title,
            Lookup= lookup,
            Author =author,
            Type = type,
            Genre = genre,
            Date_Start = ds,
            Date_Finish = df,
            Word_Count = len(words),
            Unique_Words = len(unique_words),
            Vocab_Density = vocab_density,
            Word_List= word_dict,
        )
        s.save()
    def test(self,title, author, lookup, type, genre, ds, df):
        book_string = methods.Book_Methods.clean_up(book_path+lookup)
        words, unique_words, vocab_density = methods.Book_Methods.get_stats(book_string)
        word_dict = []
        for w in words:
            word_dict.append(w)
        word_dict = Counter(word_dict)
        word_dict = json.dumps(list(sorted(word_dict.items())))
