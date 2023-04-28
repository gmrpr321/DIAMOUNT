from django.urls import path,include
from .views import ImageGenerator
urlpatterns = [
    path('',ImageGenerator.as_view(),name ="text")
]
