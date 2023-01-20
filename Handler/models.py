from django.db import models

class SignUp_info(models.Model):
    User = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User

