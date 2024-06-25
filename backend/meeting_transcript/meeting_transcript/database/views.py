from django.http import HttpResponse
from rest_framework import viewsets
from .models import CallRecord, MeetingCall, MeetingProtocol
from .serializers import CallRecordSerializer, MeetingCallSerializer, MeetingProtocolSerializer, MeetingCallCreateSerializer
from rest_framework.response import Response
from rest_framework import status
import logging


logger = logging.getLogger(__name__)


def index(request):

    return HttpResponse("Hello, world. You're at the database index.")

# Create your views here.



class MeetingCallViewSet(viewsets.ModelViewSet):
    queryset = MeetingCall.objects.all()
    serializer_class = MeetingCallSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # Use the new serializer to return only the sys_id
        return_serializer = MeetingCallCreateSerializer(serializer.instance)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MeetingProtocolViewSet(viewsets.ModelViewSet):
    queryset = MeetingProtocol.objects.all()
    serializer_class = MeetingProtocolSerializer

class CallRecordViewSet(viewsets.ModelViewSet):
    queryset = CallRecord.objects.all()
    serializer_class = CallRecordSerializer
    