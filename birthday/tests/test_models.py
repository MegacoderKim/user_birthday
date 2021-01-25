import pytest
from datetime import date
from birthday.models import UserBirthday


@pytest.mark.django_db
def test_user_birthday_create():
    user_one = UserBirthday.objects.create(
        first_name="Birthday User",
        last_name="Last Name",
        email="kimkim@test.com",
        birthday=date.fromisoformat("1999-12-04"),
    )

    assert UserBirthday.objects.count() == 1
    assert str(user_one) == "Birthday User Last Name"
