from unicodedata import category
from django.contrib import admin

from .models import Feedback

admin.site.register(Feedback)
