from django.urls import path, include
from .views import *

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz),
]