from django.urls import path
from Anamnez.views import(
    AnamnezCreateAPIView,
    AnamnezListAPIView,
    AnamnezDetailAPIView
)

urlpatterns = [
    path('create', AnamnezCreateAPIView.as_view()),
    path('list', AnamnezListAPIView.as_view()),
    path('detail/<int:pk>', AnamnezDetailAPIView.as_view())
]