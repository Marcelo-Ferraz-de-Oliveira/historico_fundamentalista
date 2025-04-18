import cloudscraper
import pandas as pd
from django.core.mail import send_mail
from historico.models import Acao  # Importando o modelo Django

def importar():
    #Scraper para a cloudflare
    url = 'https://www.fundamentus.com.br/resultado.php'
    scraper = cloudscraper.create_scraper()
    html = scraper.get(url).content
    try:
        df = pd.read_html(html,decimal=",",thousands='.')
    except:
        return False

    #o pandas retorna uma lista de dataframes - cada tabela da página gera um dataframe diferente
    #temos então que ver todos os dataframes gerados
    for d in df:
        print(d.head(10))
        print(d.dtypes)

    #como só foi criado um dataframe, ele será o padrão
    df = df[0]

    #transforma as colunas que ainda são string em float, retirando os percentuais
    listaPc = list(df.dtypes[df.dtypes == 'object'].index)
    for item in listaPc:
        if item == "Papel": continue
        df[item] = df[item].str.replace("%","")
        df[item] = df[item].str.replace(".","")
        df[item] = df[item].str.replace(",",".")
        df[item] = df[item].astype('float64')

    #dropa o Liq.2meses = 0 - são as ações que não são mais negociadas
    dfValido = df[df["Liq.2meses"] != 0]

    #calcula o P/L*P/VPA
    dfValido["PLPVPA"] = dfValido['P/L']*dfValido['P/VP']

    # #filtra de acordo com os filtros fundamentalistas
    # dfGraham = dfValido[dfValido['PLPVPA'] <= 22.5]
    # dfGraham = dfGraham[dfGraham['PLPVPA'] > 0]
    # dfGraham = dfGraham[dfGraham['P/L'] > 0]
    # dfGraham = dfGraham[dfGraham['Cresc. Rec.5a'] > 0]
    # dfGraham = dfGraham[dfGraham['P/EBIT'] > 0]
    # dfGraham = dfGraham[dfGraham['Div.Yield'] > 0]
    # dfGraham = dfGraham[dfGraham['P/Cap.Giro'] > 0]
    # dfGraham = dfGraham[dfGraham['P/Ativ Circ.Liq'] > 0]
    # dfGraham = dfGraham[dfGraham['Div.Yield'] > 6]

    # #pega os 30 menores valores de p/ebit e ordena pelo p/l
    # resultado = dfGraham.sort_values(by=['P/EBIT']).head(60).sort_values(by=['P/VP'], ascending=[True])

    # Adicionando os dados ao modelo Django
    for _, row in dfValido.iterrows():
        Acao.objects.update_or_create(
            papel=row['Papel'],
            cotacao=row['Cotação'],
            pl=row['P/L'],
            pvp=row['P/VP'],
            psr=row['PSR'],
            div_yield=row['Div.Yield'],
            pativo=row['P/Ativo'],
            pcap_giro=row['P/Cap.Giro'],
            pebit=row['P/EBIT'],
            pativ_circ_liq=row['P/Ativ Circ.Liq'],
            ev_ebit=row['EV/EBIT'],
            ev_ebitda=row['EV/EBITDA'],
            mrg_ebit=row['Mrg Ebit'],
            mrg_liq=row['Mrg. Líq.'],
            liq_corr=row['Liq. Corr.'],
            roic=row['ROIC'],
            roe=row['ROE'],
            liq_2_meses=row['Liq.2meses'],
            patrim_liq=row['Patrim. Líq'],
            div_brut_patrim=row['Dív.Brut/ Patrim.'],
            cresc_rec_5a=row['Cresc. Rec.5a'],
            plpvpa=row['PLPVPA'],
            data=pd.Timestamp.now().date()
        )
    # Envia um email confirmando a conclusão da importação
    send_mail(
        subject='Importação Concluída com Sucesso',
        message=f'A importação dos dados do Fundamentus foi concluída com sucesso em {pd.Timestamp.now().date()}.',
        from_email='nao-responda@srv684043.hstgr.cloud',
        recipient_list=['mfogoiania@gmail.com'],
        fail_silently=False,
    )
    return True