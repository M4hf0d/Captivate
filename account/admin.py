from django.contrib import admin
from .models import CustomUser, Industry, Investing, Founding, Advising
from django.contrib.auth.hashers import make_password

admin.site.register(Industry)
admin.site.register(Investing)
admin.site.register(Founding)
admin.site.register(Advising)

class CustomUserAdmin(admin.ModelAdmin):
    # Hash the passwd 
    def save_model(self, request, obj, form, change):
        if form.initial.get('password') != form.cleaned_data.get('password'):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
admin.site.register(CustomUser, CustomUserAdmin)

