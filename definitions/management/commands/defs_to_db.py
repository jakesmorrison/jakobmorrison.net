__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import Words
from .. import methods
import pandas as pd
import numpy as np
import json
from collections import Counter
import os
from PyDictionary import PyDictionary


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('text_file_path')

    def handle(self, *args, **options):
        self.def_to_db(options['text_file_path'])

    def def_to_db(self, text_file_path):
        dictionary = PyDictionary()
        words = open(text_file_path,'r')
        word_list = []
        [word_list.append(x.strip()) for x in words]

        for w in word_list:
            definition = dictionary.meaning(w)
            try:
                t = (", ".join(list(definition.keys())))
                mydef = ("\n".join(list(definition.values())[0]))
            except:
                t = ""
                mydef = ""

            if w in [x["word"] for x in Words.objects.values()]:
                pass
            else:
                s = Words(
                    word=w,
                    type= t,
                    definition=mydef,
                    frequency = 0,
                )
                s.save()
