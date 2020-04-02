from django.urls import path
from Fizikakan.views import(
    FizikakanCreateAPIView,
    FizikakanListAPIView,
    FizikakanDetailAPIView
)

urlpatterns = [
    path('create', FizikakanCreateAPIView.as_view()),
    path('list', FizikakanListAPIView.as_view()),
    path('detail/<int:pk>', FizikakanDetailAPIView.as_view())
]