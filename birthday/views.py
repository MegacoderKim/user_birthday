import json

from django.core.cache import cache
from django.conf import settings
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters import rest_framework as filters

from .models import UserBirthday
from .serializers import UserBirthdaySerializer
from .filters import BirthDateFilter


class UserBirthdayCreateListView(CreateAPIView):
    """
    Create userbithday objects from a posted list
    """

    model = UserBirthday
    serializer_class = UserBirthdaySerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=json.loads(request.data), many=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            cache.delete(settings.AVERAGE_AGE_KEY)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBirthDayList(ListAPIView):
    """
    Get user birthday list with filters
    """

    queryset = UserBirthday.objects.all()
    serializer_class = UserBirthdaySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BirthDateFilter


class GetAverageAge(APIView):
    """
    Return the average count of birthdays
    """

    def get(self, request):
        all_birthdays = UserBirthday.objects.all()
        average_age = cache.get(settings.AVERAGE_AGE_KEY)
        if not average_age:
            average_age = sum([z.age for z in all_birthdays]) // all_birthdays.count()
            cache.set(settings.AVERAGE_AGE_KEY, average_age)
        return Response({"average_age": average_age}, status=status.HTTP_200_OK)
