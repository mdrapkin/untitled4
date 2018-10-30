from django.db import models

class TestTable(models.Model):
    teststring = models.CharField(max_length=255)
