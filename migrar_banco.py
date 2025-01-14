from django.db import connections
from historico.models import Acao

def migrar_dados():
    # Conectando ao banco antigo e ao novo
    with connections['default'].cursor() as antigo_cursor, connections['postgres'].cursor() as novo_cursor:
        # Carregar dados do banco antigo
        for acao in Acao.objects.using('default').all():
            # Criar o mesmo registro no novo banco
            Acao.objects.using('postgres').create(
                papel=acao.papel,
                cotacao=acao.cotacao,
                pl=acao.pl,
                pvp=acao.pvp,
                psr=acao.psr,
                div_yield=acao.div_yield,
                pativo=acao.pativo,
                pcap_giro=acao.pcap_giro,
                pebit=acao.pebit,
                pativ_circ_liq=acao.pativ_circ_liq,
                ev_ebit=acao.ev_ebit,
                ev_ebitda=acao.ev_ebitda,
                mrg_ebit=acao.mrg_ebit,
                mrg_liq=acao.mrg_liq,
                liq_corr=acao.liq_corr,
                roic=acao.roic,
                roe=acao.roe,
                liq_2_meses=acao.liq_2_meses,
                patrim_liq=acao.patrim_liq,
                div_brut_patrim=acao.div_brut_patrim,
                cresc_rec_5a=acao.cresc_rec_5a,
                plpvpa=acao.plpvpa,
                data=acao.data
            )
    print("Migração concluída com sucesso!")

# Execute o script
migrar_dados()
