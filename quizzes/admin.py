from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Choice, Taker, Answer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Taker)
admin.site.register(Answer)