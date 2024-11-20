from django.contrib import admin
from burgers.models import Burgers 

@admin.register(Burgers) #버거스 테이블 admin 권한부여 
class BurgersAmin(admin.ModelAdmin):
    pass

