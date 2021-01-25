from django.urls import path

from .views import CreateBirthdayListView


urlpatterns = [
    path("userbirthdays", CreateBirthdayListView.as_view(), name="birthdays-create")
]