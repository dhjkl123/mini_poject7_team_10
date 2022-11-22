from django.db import models

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

class AiModel(models.Model):
    model_name = models.CharField(null = False, default='', max_length=250)
    model_ver = models.CharField(max_length=10)
    model_selected = models.BooleanField()
    pub_date = models.DateTimeField('date published')
    model = models.FileField()

class ModelPerformance(models.Model):
    model_name = models.CharField(null = False, default='', max_length=250)
    total = models.IntegerField()
    sucesse = models.IntegerField()
    acc = models.FloatField(null = False, default=0.0)
