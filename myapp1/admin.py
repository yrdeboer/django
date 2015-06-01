from django.contrib import admin
from .models import MyUser, MyRole, MyModel, MyPermission, KeyModel, ValueModel, PairHolder, PairUser

# Register your models here.
admin.site.register(MyRole)
admin.site.register(MyUser)
admin.site.register(MyModel)
admin.site.register(MyPermission)
admin.site.register(KeyModel)
admin.site.register(ValueModel)
admin.site.register(PairHolder)
admin.site.register(PairUser)
