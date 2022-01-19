from django.db import models

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user_name

class Equiment(models.Model):
    equip_name=models.CharField(max_length=200)

    def __str__(self):
        return self.equip_name

class Loan(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    state=models.CharField(max_length=200)
    equip_name=models.ForeignKey(Equiment, null=True, on_delete=models.SET_NULL)
    beginDate=models.DateField(auto_now=False,auto_now_add=False, null=True)
    endDate=models.DateField(auto_now=False,auto_now_add=False, null=True)
    deliveryDate=models.DateField(auto_now=False,auto_now_add=False, null=True)
    ticket=models.FloatField(default=0)


