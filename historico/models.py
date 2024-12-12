from django.db import models

class Acao(models.Model):
    papel = models.CharField(max_length=10)
    cotacao = models.FloatField()
    pl = models.FloatField()  # Preço sobre lucro
    pvp = models.FloatField()  # Preço sobre valor patrimonial
    psr = models.FloatField()  # Preço sobre receita
    div_yield = models.FloatField()  # Dividend yield
    pativo = models.FloatField()  # Preço sobre ativo
    pcap_giro = models.FloatField()  # Preço sobre capital de giro
    pebit = models.FloatField()  # Preço sobre EBIT
    pativ_circ_liq = models.FloatField()  # Preço sobre ativo circulante líquido
    ev_ebit = models.FloatField()  # Valor da empresa sobre EBIT
    ev_ebitda = models.FloatField()  # Valor da empresa sobre EBITDA
    mrg_ebit = models.FloatField()  # Margem EBIT
    mrg_liq = models.FloatField()  # Margem líquida
    liq_corr = models.FloatField()  # Liquidez corrente
    roic = models.FloatField()  # Retorno sobre capital investido
    roe = models.FloatField()  # Retorno sobre patrimônio
    liq_2_meses = models.FloatField()  # Liquidez nos últimos 2 meses
    patrim_liq = models.FloatField()  # Patrimônio líquido
    div_brut_patrim = models.FloatField()  # Dívida bruta sobre patrimônio
    cresc_rec_5a = models.FloatField()  # Crescimento da receita em 5 anos
    plpvpa = models.FloatField()  # PL/PVPA
    data = models.DateField()

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"

    def __str__(self):
        return f"{self.papel} - {self.cotacao} - {self.data}"
