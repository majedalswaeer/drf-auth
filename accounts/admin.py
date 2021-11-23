from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    model=CustomUser
    fieldset=UserAdmin.fieldsets 
    add_fieldsets=((None,{'fields':('username','email','first_name','last_name','password')}),)
admin.site.register(CustomUser,CustomUserAdmin)
