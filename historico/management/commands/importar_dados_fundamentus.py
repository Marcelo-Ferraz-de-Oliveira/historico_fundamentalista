# nome_do_aplicativo/management/commands/meu_comando.py
from django.core.management.base import BaseCommand
from historico import importar_fundamentus
from time import sleep

class Command(BaseCommand):
    help = 'Importa os dados do fundamentus e salva'

    def handle(self, *args, **kwargs):
        espera = 60
        if not importar_fundamentus.importar():
            print(f'Não foi possível importar. Tentando novamente em {espera} segundos')
            sleep(espera)
            self.handle(self, *args, **kwargs)
        else:
            print("Importação concluída")