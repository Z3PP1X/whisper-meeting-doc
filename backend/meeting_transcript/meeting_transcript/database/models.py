from django.db import models
import uuid
import hashlib


class MeetingCall(models.Model):
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
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
    
class MeetingProtocol(models.Model):
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
    content = models.JSONField()
    meeting_call = models.ForeignKey(MeetingCall, on_delete=models.CASCADE, related_name='meeting_protocols')

    def save(self, *args, **kwargs):
        if not self.sys_id:
            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sys_id


class CallRecord(models.Model):
    timestamp = models.JSONField()
    sys_id = models.CharField(max_length=64, unique=True, blank=True)
    call_id = models.CharField(max_length=50)
    caller_id = models.CharField(max_length=50)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    payload = models.FileField(upload_to='audio/')
    transcription = models.TextField()
    meeting_call = models.ForeignKey(MeetingCall, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.sys_id:
            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.sys_id