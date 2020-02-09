from django.db import models
# from celery.worker.strategy import default

# Create your models here.
class ResultPoolService(models.Model):
    ticket = models.CharField(primary_key=True, max_length=200)
    text = models.TextField()
    pool = models.IntegerField(default=0)
    
class PoolCompare(models.Model):
    result_pool = models.IntegerField()
    service_pool = models.IntegerField()