from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse  # To generate URLS by reversing URL patterns
import uuid  # Required for unique book instances
# Create your models here.

class Blog(models.Model):
    """Model representing a blog post written by an author"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(help_text="Bring your ideas to reality")
    
    class Meta:
        ordering = ['date']
    
    def get_absolute_url(self):
        """Returns the url to access a particular language instance."""
        return reverse('blog-detail', args=[str(self.id)])
    
    def __str__(self):
            """String for representing the Model object."""
            return f'{self.title}'

class Comment(models.Model):
    """Model representing a comment under a blog post written by a logged in user"""
    user = models.ForeignKey('User', on_delete=models.RESTRICT, null=True)
    text = models.TextField(max_length=1000, help_text="Display your opinion about this blog post to the rest of the world")
    blog = models.ForeignKey(
        'Blog', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular comment across blogs")
    class Meta:
        ordering = ['date']

    def __str__(self):
            """String for representing the Model object."""
            return f'{self.text[:10]}, {self.blog}'

class User(AbstractUser):
    """Model representing a logged in User who can comment"""
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
            """String for representing the Model object."""
            return f'{self.name}'

class Author(models.Model):
    """Model representing a logged in User, who can write blogs"""
    name = models.ForeignKey('User', on_delete=models.CASCADE)
    bioinformation = models.TextField(max_length=1000, help_text="Enter a brief description about yourself")

    def __str__(self):
            """String for representing the Model object."""
            return f'{self.name}'
