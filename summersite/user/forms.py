from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import MyUser

# form for sign-up view
class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'wechat_id')


# form for change user profile view
class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ('username',)
        fieldsets = (
            ('User Information', {'fields': ('username', 'password')}),
            ('Personal Information', {'fields': ('wechat_id', 'first_name', 'last_name', 'email')}),
            ('Permissions', {'fields': ('is_tutor', 'is_staff', 'is_superuser', 'is_active')}),
            ('Important Dates', {'fields': ('last_login', 'date_joined')})
        )
        list_display = (
            'username', 
            'wechat_id', 
            'first_name', 
            'last_name', 
            'is_tutor', 
            'is_staff', 
            'is_active'
        )


