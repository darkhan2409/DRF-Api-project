from .views import *
from django.urls import path


urlpatterns = [
    path('', PlatformApiView.as_view()),
]
