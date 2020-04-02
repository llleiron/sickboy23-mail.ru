from django.urls import path
from Tsarayutyun.views import(
    TsarayutyunCreateAPIView,
    TsarayutyunListAPIView,
    TsarayutyunDetailAPIView
)

urlpatterns = [
    path('create', TsarayutyunCreateAPIView.as_view()),
    path('list', TsarayutyunListAPIView.as_view()),
    path('detail/<int:pk>', TsarayutyunDetailAPIView.as_view())
]