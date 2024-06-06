from django.db import models
import uuid
import hashlib
import meeting_call
import meeting_protocol



class call_record(models.Model):

    timestamp = models.JSONField()
    sys_id = models.CharField()
    call_id = models.CharField(max_length=50)
    caller_id = models.CharField(max_length=50)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    payload = models.FileField(upload_to='audio/')
    transcription = models.TextField()
    meeting_call = models.ForeignKey(meeting_call, on_delete=models.CASCADE, related_name='call_record')
    meeting_protocol = models.ForeignKey(meeting_protocol, on_delete=models.CASCADE, related_name='call_record')

    def save(self, *args, **kwargs):

        if not self.sys_id:

            self.sys_id = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()

        super().save(*args, **kwargs)

    def __str__(self):

        return self.sys_id
    

