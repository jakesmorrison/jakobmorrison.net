__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import Stats
import pandas as pd
import numpy as np

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type')

    def handle(self, *args, **options):
        self.convert_csv_to_db(options['type'])

    def convert_csv_to_db(self, csv_path):
        df = pd.read_csv(csv_path)
        df = df.fillna(value=0)
        for index, row in df.iterrows():
            s = Stats(
                season=row["Season"],
                date= str(row["Date"].split("/")[2]+"-"+row["Date"].split("/")[0]+"-"+row["Date"].split("/")[1]),
                player =row["Player"],
                games = row["Games"],
                pa = row["PA"],
                ab = row["AB"],
                bb = row["BB"],
                so = row["SO"],
                hidp = row["HIDP"],
                cs = row["CS"],
                dbo=row["DBO"],
                sb=row["SB"],
                h=row["H"],
                firstb=row["1B"],
                secondb=row["2B"],
                thirdb=row["3B"],
                fourthb=row["4B"],
                hr = row["HR"],
                r = row["R"],
                rbi = row["RBI"]
            )
            s.save()