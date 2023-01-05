from django.contrib import admin
from .models import User


admin.site.site_header  =  "Nusah Audio"
admin.site.site_title  =  "Nusah Account"
admin.site.index_title  =  "Nusah Audio Account Adminstration"


class  userAdmin(admin.ModelAdmin):
    list_display=('id','email','age','date_joined','is_active','is_staff','avatar','username')
    search_fields = ['username','age','email']

admin.site.register(User, userAdmin)

