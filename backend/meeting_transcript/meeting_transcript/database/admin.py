from django.contrib import admin

from .models import CallRecord, MeetingCall, MeetingProtocol

admin.site.register(MeetingCall)
admin.site.register(MeetingProtocol)
admin.site.register(CallRecord) 
