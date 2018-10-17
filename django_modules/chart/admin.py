from django.contrib import admin
from .models import Chart
from .models import TypeChart


class ChartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chart, ChartAdmin)


class TypeChartAdmin(admin.ModelAdmin):
    pass

admin.site.register(TypeChart, TypeChartAdmin)
