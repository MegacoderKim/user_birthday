from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
import json

from .models import UserBirthday
from .serializers import UserBirthdaySerializer


class CreateBirthdayListView(CreateAPIView):
    """
    Create userbithday objects from a posted list
    """

    model = UserBirthday
    serializer_class = UserBirthdaySerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=json.loads(request.data), many=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
