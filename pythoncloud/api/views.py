from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from .models import Timestamp
from .serializers import TimestampCreateSerializer


class TimestampCreateView(ListCreateAPIView):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampCreateSerializer
