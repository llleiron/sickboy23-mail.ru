from django.urls import path
from YndhanurTexekutyunner.views import(
    YndhanurTexekutyunnerCreateAPIView,
    YndhanurTexekutyunnerListAPIView,
    YndhanurTexekutyunnerDetailAPIView
)

urlpatterns = [
    path('create', YndhanurTexekutyunnerCreateAPIView.as_view()),
    path('list', YndhanurTexekutyunnerListAPIView.as_view()),
    path('detail/<int:pk>', YndhanurTexekutyunnerDetailAPIView.as_view())
]