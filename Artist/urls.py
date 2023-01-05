from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Artist import views
from django.urls import re_path


urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artist/<int:pk>/', views.ArtistDetail.as_view()),
]