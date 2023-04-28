from django.urls import path,include
from .views import Textview
urlpatterns = [
    path('',Textview.as_view(),name ="text")
]
