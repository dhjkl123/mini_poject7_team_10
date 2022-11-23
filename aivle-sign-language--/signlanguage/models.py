from django.db import models
from django.db import transaction
# from django.db.models import constraints
# from django.db.models.query_utils import Q
# from picklefield.fields import PickledObjectField

# Create your models here.

class Result(models.Model):
    image = models.ImageField(blank=True)
    answer = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published')

    
class AI_Model(models.Model):
    # realModel = PickledObjectField()
    model_Name = models.CharField(max_length=50)
    model_Version = models.CharField(max_length=50, null=True)
    model_File = models.FileField(upload_to='model/')
    create_Date = models.DateField(auto_now=True)
    is_selected = models.BooleanField(default=True)
    
    # if is_selected:
        
    # def save(self, *args, **kwargs):
    #     if self.is_selected:
    #         self.objects.filter(is_selected=True).update(is_selected=False)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Name : {self.model_Name}, Date : {self.create_Date}'

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['is_selected'], condition=Q(is_selected=True), name='unique_is_selected')
    #     ]
    
    def save(self, *args, **kwargs):
        if not self.is_selected:
            return super(AI_Model, self).save(*args, **kwargs)
        with transaction.atomic():
            AI_Model.objects.filter(
                is_selected=True).update(is_selected=False)
            return super(AI_Model, self).save(*args, **kwargs)
