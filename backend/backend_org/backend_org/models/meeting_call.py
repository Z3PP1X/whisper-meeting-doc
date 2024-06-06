from django.db import models
import hashlib
import uuid

class meeting_call(models.Model):

    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    sys_id = models.CharField(max_length=64)
    attendees = models.JSONField()
    meeting_date = models.DateTimeField()
    meeting_topic = models.CharField(max_length=100)
    meeting_start_time = models.DateTimeField()
    meeting_end_time = models.DateTimeField()
    duration = models.DurationField()
    





    def save(self, *args, **kwargs):

        if not self.sys_id:

            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.sys_id