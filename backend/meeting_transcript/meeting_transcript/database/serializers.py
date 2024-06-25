from rest_framework import serializers
from .models import CallRecord, MeetingCall, MeetingProtocol

class MeetingCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingCall
        fields = '__all__'

class MeetingCallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingCall
        fields = ['sys_id']

class MeetingProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingProtocol
        fields = '__all__'

class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = '__all__'