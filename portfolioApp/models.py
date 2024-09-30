from django.db import models

class ContactFormDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    class Meta:
        db_table = "ContactFormDetails"

    def __str__(self):
        return self.name
