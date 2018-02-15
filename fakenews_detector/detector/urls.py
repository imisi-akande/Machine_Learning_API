from django.urls import path

from . import views

urlpatterns = [
    path(r'news/', views.DetectorList.as_view()),
    path(r'^news/$', views.DetectorList.as_view()),
    path(r'news/<int:pk>/', views.DetectorDetail.as_view()),
]