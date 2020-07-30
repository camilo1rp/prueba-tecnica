from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'contacts'
