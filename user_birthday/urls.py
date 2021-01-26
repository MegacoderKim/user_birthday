from django.urls import path, include
from rest_framework.documentation import include_docs_urls

apipatterns = [path("", include("birthday.urls"))]

urlpatterns = [
    path("", include_docs_urls(title="Birthdays API")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1", include(apipatterns)),
]
