from django.contrib import admin

# Register your models here.
from .models import Students, Admissions, College, Gkorder
admin.site.register(Students)
admin.site.register(Admissions)
admin.site.register(College)
admin.site.register(Gkorder)