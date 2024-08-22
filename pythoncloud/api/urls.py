from django.urls import path, include

from .views import TimestampCreateView

urlpatterns = [
    path("timestamp/", TimestampCreateView.as_view())
]
