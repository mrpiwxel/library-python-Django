from django.db import models

class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        genre = models.CharField(max_length=50)
        available = models.BooleanField(default=True)
        isBorrowed = models.BooleanField(default=False)
        borrowerName = models.CharField(max_length=50,null=True)
        borrowerNumber = models.CharField(max_length=11,null=True)
        borrow_date = models.CharField(max_length=11,null=True)
        return_date = models.CharField(max_length=11,null=True)      
