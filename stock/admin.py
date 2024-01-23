from django.contrib import admin
from stock.models import Stock, Currency

# Register your models here.
from stock.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description")
    pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
