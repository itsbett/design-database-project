from django.contrib import admin
from .models import Customer, Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('custID', 'login', 'name', 'address', 'phone')

# Register your models here.
admin.site.register(Todo, TodoAdmin)
admin.site.register(Customer, CustomerAdmin)