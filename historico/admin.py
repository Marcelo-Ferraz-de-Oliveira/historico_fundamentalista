from django.contrib import admin
from .models import Acao

class PLPVPFilter(admin.SimpleListFilter):
    title = 'PL e PVP'
    parameter_name = 'pl_pvp'

    def lookups(self, request, model_admin):
        return (
            ('low', 'PL > 0 e PVP > 0'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(pl__gt=0, pvp__gt=0)
        return queryset

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('papel', 'cotacao', 'pl', 'pvp', 'div_yield', 'roic', 'roe', 'data')
    search_fields = ('papel',)
    list_filter = ('data', PLPVPFilter)