from django.contrib import admin
from .models import Question, Team

# Register your models here.
admin.site.register(Team)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'set_number', 'order_number')
    fieldsets = (
        (None, {
            'fields': (
                'question_text',
                'answer_text',
                'set_number',
                'order_number'
            )
        }),
    )


admin.site.register(Question, QuestionsAdmin)
