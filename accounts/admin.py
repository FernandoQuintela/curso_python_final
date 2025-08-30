from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {'fields': ('avatar', 'bio', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra info', {'fields': ('avatar', 'bio', 'birth_date')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
