from django.urls import path

from .views import UserBirthdayCreateListView, UserBirthDayList, GetAverageAge


urlpatterns = [
    path(
        "userbirthdays", UserBirthdayCreateListView.as_view(), name="birthdays-create"
    ),
    path("userbirthdayslist", UserBirthDayList.as_view(), name="birthdays-list"),
    path("usersaverageage", GetAverageAge.as_view(), name="average_age"),
]