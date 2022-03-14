import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "[{},{}]".format(self.question_text,self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    #CASCADE: When the referenced object is deleted, also delete the objects that have references to it 
    # (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "[{},{}]".format(self.choice_text,self.votes)