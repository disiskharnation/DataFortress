from django.db import models
from User.models import User

class ChangePassword(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_changes')
    new_password = models.CharField(max_length=255, null=False)
    change_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'ChangePassword'

class ForgotPasswordRequest(models.Model):
    request_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forgot_password_requests')
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    request_timestamp = models.DateTimeField(auto_now_add=True)
    expiry_timestamp = models.DateTimeField()

    class Meta:
        db_table = 'ForgotPasswordRequest'