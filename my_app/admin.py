from django.contrib import admin
from . models import Document,Textnotes,Comment,Questions
# Register your models here.
admin.site.register(Document)
admin.site.register(Textnotes)
admin.site.register(Comment)
admin.site.register(Questions)