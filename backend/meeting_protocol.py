from django.db import models
import uuid
import hashlib
import meeting_call

class meeting_protocol(models.Model):

    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_id = models.CharField()
    content = models.JSONField()
    meeting_call = models.ForeignKey(meeting_call, on_delete=models.CASCADE, related_name='meeting_protocol')



    def save(self, *args, **kwargs):

        if not self.sys_id:

            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.sys_id