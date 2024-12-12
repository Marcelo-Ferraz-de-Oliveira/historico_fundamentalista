Este software importa os dados fundamentalistas das ações da B3 e salva em um banco com a informação da data, montando um histórico de informações fundamentalistas.

Projeto feito com `python3.11`

Configurado para usar mongodb atlas.

Para executar o projeto:
```
python3.11 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

Para realizar a importação dos dados
```
python manage.py importar_dados_fundamentus
```