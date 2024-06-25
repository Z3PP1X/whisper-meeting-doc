from django.http import HttpResponse
from rest_framework import viewsets
from .models import CallRecord, MeetingCall, MeetingProtocol
from .serializers import CallRecordSerializer, MeetingCallSerializer, MeetingProtocolSerializer


def index(request):

    return HttpResponse("Hello, world. You're at the database index.")

# Create your views here.

class MeetingCallViewSet(viewsets.ModelViewSet):
    queryset = MeetingCall.objects.all()
    serializer_class = MeetingCallSerializer

class MeetingProtocolViewSet(viewsets.ModelViewSet):
    queryset = MeetingProtocol.objects.all()
    serializer_class = MeetingProtocolSerializer

class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer
    