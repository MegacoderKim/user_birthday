from django.urls import path, include


apipatterns = [path("", include("birthday.urls"))]

urlpatterns = [path("api/v1", include(apipatterns))]
