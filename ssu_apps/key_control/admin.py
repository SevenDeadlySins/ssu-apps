from django.contrib import admin

from .models import *

admin.site.register(UserType)
admin.site.register(KeyType)
admin.site.register(KeyStatus)
admin.site.register(Position)
admin.site.register(Sequence)
admin.site.register(Distribution)
admin.site.register(Location)