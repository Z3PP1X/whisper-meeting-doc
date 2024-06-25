from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MeetingCallViewSet, MeetingProtocolViewSet, CallRecordViewSet

router = routers.DefaultRouter()
router.register(r'meetingcall', MeetingCallViewSet)
router.register(r'meetingprotocol', MeetingProtocolViewSet)
router.register(r'callrecord', CallRecordViewSet)

urlpatterns = [
    path('', include(router.urls))
]