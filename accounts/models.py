from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    balance = models.IntegerField(default=0,)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    def __str__(self):
        return self.username


# class Transaction(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transactions')
#     amount = models.IntegerField()
#     description = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.amount} - {self.timestamp}"

# class Subscription(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscriptions')