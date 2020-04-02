from django.urls import path
from Myus.views import(
    MyusCreateAPIView,
    MyusListAPIView,
    MyusDetailAPIView
)

urlpatterns = [
    path('create', MyusCreateAPIView.as_view()),
    path('list', MyusListAPIView.as_view()),
    path('detail/<int:pk>', MyusDetailAPIView.as_view())
]