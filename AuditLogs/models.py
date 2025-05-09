from django.db import models
from User.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    ip_address = models.GenericIPAddressField()
    
    class Meta:
        db_table = 'AuditLogs'