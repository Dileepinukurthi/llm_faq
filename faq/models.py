from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Keyword(models.Model):
    name = models.CharField(max_length=100)
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='faq_keywords')

    def __str__(self):
        return self.name
