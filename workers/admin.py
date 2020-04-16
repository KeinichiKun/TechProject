from django.contrib import admin
from .models import Position, Worker, Type_work, Tabel_time
# Register your models here.

admin.site.register(Position)
admin.site.register(Worker)
admin.site.register(Type_work)
admin.site.register(Tabel_time)