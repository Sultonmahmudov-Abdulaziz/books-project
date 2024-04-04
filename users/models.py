from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

    


class Books(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='books_images/', blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

class Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class BooksAutor(models.Model):
    books = models.ForeignKey(Books,on_delete=models.CASCADE)
    authors = models.ForeignKey(Author,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.books.name} by {self.authors.first_name} {self.authors.last_name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment_text = models.TextField()
    stars_given = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    def __str__(self):
        return f"{self.user} commented to {self.book.name} and gave {self.stars_given} stars"
        


    
