from django.urls import path
from Grancum.views import(
    GrancumCreateAPIView,
    GrancumDetailAPIView,
    GrancumListAPIView
)

urlpatterns = [
    path('create', GrancumCreateAPIView.as_view()),
    path('list', GrancumListAPIView.as_view()),
    path('detail/<int:pk>', GrancumDetailAPIView.as_view())
]