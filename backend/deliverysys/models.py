from django.db import models

# Create your models here.
# --- NEED TO UPDATE WITH CURRENT TABLES

class Customer(models.Model):
    custID = models.IntegerField(primary_key = True)
    login = models.CharField(blank = False, max_length = 255)
    name = models.CharField(blank = False, max_length = 255)
    address = models.CharField(blank = False, max_length = 255)
    phone = models.CharField(blank = False, max_length = 255)

    def _str_(self):
        return self.custID

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title