from django.db import models

# Models


class UserData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
