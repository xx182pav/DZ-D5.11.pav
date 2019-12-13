from django.db import models

# Create your models here.
  
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

def __str__(self):
    return self.full_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    copy_count = models.SmallIntegerField(default = 1)

def __str__(self):
        return self.title 


class Redaction(models.Model):
    name = models.TextField(max_length=128)
    creation_year = models.SmallIntegerField()
    description = models.TextField()
    
def __str__(self):
        return self.name

class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works",
    )
    
class Friend(models.Model):
    friend_name = models.CharField(max_length=30)
    borrowed_books = models.ManyToManyField(Book)

def __str__(self):
    return self.friend_name


