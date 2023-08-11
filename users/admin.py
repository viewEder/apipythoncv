from django.contrib import admin
from .models import User, ResumeUser, Links

# Register your models here.
admin.site.register(User)
admin.site.register(ResumeUser)
admin.site.register(Links)
