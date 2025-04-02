from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class GSTDeclaration(models.Model):
    gst_number = models.CharField(max_length=15, unique=True)
    date_of_filing = models.DateField()
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    pan_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # To track submission time

    def __str__(self):
        return f"GST: {self.gst_number} | PAN: {self.pan_number}"