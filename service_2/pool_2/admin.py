from django.contrib import admin

# Register your models here.
from .models import ResultPoolService, PoolCompare

class PoolCompareAdmin(admin.ModelAdmin):
    fields = ['result_pool', 'service_pool']
    list_display = ('result_pool', 'service_pool')
     
class ResultPoolAdmin(admin.ModelAdmin):
    fields = ['ticket', 'text', 'pool']
    list_display = ('ticket', 'text', 'pool')
 
admin.site.register(ResultPoolService, ResultPoolAdmin)
admin.site.register(PoolCompare, PoolCompareAdmin)