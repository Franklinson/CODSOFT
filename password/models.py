from django.db import models

# Create your models here.
class Password(models.Model):
    password = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.password