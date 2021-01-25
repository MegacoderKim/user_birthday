from django_filters import rest_framework as filters
from .models import UserBirthday


class BirthDateFilter(filters.FilterSet):
    _from = filters.DateFilter(field_name="birthday", lookup_expr="gte")
    to = filters.DateFilter(field_name="birthday", lookup_expr="lte")

    class Meta:
        model = UserBirthday
        fields = ["_from", "to"]
