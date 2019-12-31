from django.contrib import admin
from .models import Venue, MyclubUser, Event
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
#from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)
admin.site.register(Venue)
admin.site.register(MyclubUser)
admin.site.register(Event)
#admin.site.register(User, UserAdmin)