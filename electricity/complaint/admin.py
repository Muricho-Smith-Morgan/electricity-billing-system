from django.contrib import admin
from .models import Complaint

# Register your models here.
@admin.register(Complaint)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'residence', 'problem', 'email', 'phone_number', 'status']