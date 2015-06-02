from django.contrib import admin
from .models import MyUser, MyRole, MyModel, MyPermission, KeyModel, ValueModel, PairHolder, PairUser, OSPPermission, OSPRole, OSPModel1, OSPModel2

# Register your models here.
admin.site.register(MyRole)
admin.site.register(MyUser)
admin.site.register(MyModel)
admin.site.register(MyPermission)
admin.site.register(KeyModel)
admin.site.register(ValueModel)
admin.site.register(PairHolder)
admin.site.register(PairUser)
admin.site.register(OSPPermission)
admin.site.register(OSPRole)
admin.site.register(OSPModel1)
admin.site.register(OSPModel2)
