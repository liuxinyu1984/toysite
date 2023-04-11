from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


# customized UserAdmin class, modify the user page in admin panel
# class MyUserAdmin(UserAdmin):
#     # add the custom field 'wechat_id' to the admin panel
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Additional Info', {
#                 'fields':(
#                     'wechat_id',
#                     'is_tutor'
#                 )
#             }
#         )
#     )
#     # modify display list of MyUsers, only showing the following 5 fields in list
#     list_display = ('username', 'wechat_id', 'first_name', 'last_name', 'is_tutor', 'is_staff', 'is_active')

# admin.site.register(MyUser, MyUserAdmin)


# change the ordering of fields of users, in the user profile page in admin panel
fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('wechat_id', 'first_name', 'last_name', 'email')})
fields[2] = ('Permissions', {'fields': ('is_tutor', 'is_staff', 'is_superuser', 'is_active')})
UserAdmin.fieldsets = tuple(fields)

# change the display order of fields in the user list in admin panel
UserAdmin.list_display = (
    'username', 
    'wechat_id', 
    'first_name', 
    'last_name', 
    'is_tutor', 
    'is_staff', 
    'is_active'
)

# register the modified UserAdmin class
admin.site.register(MyUser, UserAdmin)