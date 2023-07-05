from django.urls import path
from .views import *

urlpatterns = [
    path('check-content/', originalAITest.as_view()),
]