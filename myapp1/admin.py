from django.contrib import admin
from .models import MyUser, MyRole, MyModel, MyPermission

# Register your models here.
admin.site.register(MyRole)
admin.site.register(MyUser)
admin.site.register(MyModel)
admin.site.register(MyPermission)

