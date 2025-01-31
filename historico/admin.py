from django.contrib import admin
from .models import Acao

class PLPVPFilter(admin.SimpleListFilter):
    title = 'PL e PVP'
    parameter_name = 'pl_pvp'

    def lookups(self, request, model_admin):
        return (
            ('low', 'PL < 10 e PVP < 1'),
            ('mid', 'PL 10-20 e PVP 1-2'),
            ('high', 'PL > 20 e PVP > 2'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(pl__lt=10, pvp__lt=1)
        if self.value() == 'mid':
            return queryset.filter(pl__gte=10, pl__lte=20, pvp__gte=1, pvp__lte=2)
        if self.value() == 'high':
            return queryset.filter(pl__gt=20, pvp__gt=2)
        return queryset

@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('papel', 'cotacao', 'pl', 'pvp', 'div_yield', 'roic', 'roe', 'data')
    search_fields = ('papel',)
    list_filter = ('data', PLPVPFilter)