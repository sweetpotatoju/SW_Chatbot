from django.contrib import admin
from .models import Notice
from .models import QATable

admin.site.register(Notice)
admin.site.register(QATable)