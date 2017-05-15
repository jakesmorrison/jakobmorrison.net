
__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import Polls

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.add_poll()

    def add_poll(self):
        p = Polls(
            question="Grak ran Lucas off his base. What should go down in the stat book?",
            poss= {
                "Grak 3B. Lucas CS.":0,
                "Grak 3B and CS.":0,
                "Grak 2B. Lucas CS.":0,
                "Grak 2B and CS.":0,
                "We should be more concerned about winning games.":0,
                "This is stupid and I dont care.":0,
            }
        )
        p.save()
