import pytest
from datetime import date
from birthday.models import UserBirthday
from birthday.serializers import UserBirthdaySerializer


@pytest.mark.django_db
def test_user_birthday_serialization():
    user_one = UserBirthday.objects.create(
        first_name="Birthday",
        last_name="Last Name",
        email="kimkim@test.com",
        birthday=date.fromisoformat("2000-12-04"),
    )

    birthday_user = UserBirthdaySerializer(user_one)
    serialized_object = birthday_user.data
    assert serialized_object["first_name"] == "Birthday"
    assert serialized_object["last_name"] == "Last Name"
    assert serialized_object["email"] == "kimkim@test.com"
    assert serialized_object["birthday"] == "2000-12-04"
