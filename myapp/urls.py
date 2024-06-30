

from django.urls import path,include
from . import views
urlpatterns = [
    path('home',views.home),
    path('summarize',views.summarization),
    path('generate_audio',views.generate_audio),
    path('generate_powerpoint',views.generate_powerPoint),
    path('generate_video',views.generate_video),
    path('powerpoint_success/<int:id>/',views.powerpoint_success)
]