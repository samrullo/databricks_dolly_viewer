from django.contrib import admin

# Register your models here.
from .models import DatabrickModel

admin.site.register(DatabrickModel)