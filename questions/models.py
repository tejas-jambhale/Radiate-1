from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.template.defaultfilters import truncatechars


class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_text = models.TextField()
    answer_text = models.CharField(max_length=500)
    set_number = models.IntegerField(choices=[(i, i) for i in range(1, 16)], blank=True)
    order_number = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)

    def __str__(self):
        return truncatechars(self.question_text, 40)


class Team(models.Model):
    name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    set_selected = models.IntegerField(choices=[(i, i) for i in range(1, 16)], blank=True)
    current_question = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)