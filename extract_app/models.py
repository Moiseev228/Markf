from django.db import models

# Create your models here.

class Recepts(models.Model):
    id_prepations = models.IntegerField(default=1)
    id_patiens = models.IntegerField(default=1)
    id_staff = models.IntegerField(default=1)
    Exemption = models.CharField(max_length = 20, default = 'Не льготный')
    Type_exemption = models.CharField(max_length = 50, default = ' ')
    date_issue = models.CharField(max_length = 8)