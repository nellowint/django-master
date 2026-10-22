
import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from apps.actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file-name',
            type=str,
            help='Informar o caminho do arquivo CSV',
        )

    def handle(self, *args, **options):
        try:
            file_name = options['file-name']

            with open(file_name, 'r', encoding='utf-8') as file:
                self.stdout.write(self.style.SUCCESS('Iniciando Importação'))
                reader = csv.DictReader(file)

                actors = [
                    Actor(
                        name=row['name'],
                        birthday=self.__get_date(row['birthday']),
                        nationality=row['nationality'],
                    ) for row in reader
                ]

                Actor.objects.bulk_create(actors)
                self.stdout.write(self.style.SUCCESS('Importação concluída'))
        except ImportError:
            self.stdout.write(self.style.ERROR('Erro na Importação'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Arquivo CSV não encontrado'))

    def __get_date(self, value):
        return datetime.strptime(value, '%Y-%m-%d').date()
