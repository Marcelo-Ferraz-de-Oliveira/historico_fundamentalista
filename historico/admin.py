from django.contrib import admin
from .models import Acao

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('papel', 'cotacao', 'pl', 'pvp', 'div_yield', 'roic', 'roe', 'data')
    search_fields = ('papel',)
    list_filter = ('data', 'papel')