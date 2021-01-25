import pytest
import json
from django.urls import reverse
from birthday.models import UserBirthday


@pytest.mark.django_db
def test_success_creation_of_birthdays(api_client):
    url = reverse("birthdays-create")
    post_data = [
        {
            "first_name": "Eike",
            "last_name": "Bartels",
            "email": "bartels@baumeister-rosing.de",
            "birthday": "01.03.1989",
        },
        {
            "first_name": "Hans",
            "last_name": "Peter",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "30.03.1989",
        },
    ]
    response = api_client.post(url, json.dumps(post_data), format="json")
    assert response.status_code == 201
    assert len(response.json()) == 2
    assert UserBirthday.objects.count() == 2


@pytest.mark.django_db
def test_failure_creation_of_birthdays_nonunique_email(api_client):
    url = reverse("birthdays-create")
    post_data = [
        {
            "first_name": "Hans",
            "last_name": "Peter",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "30.03.1989",
        },
    ]
    UserBirthday.objects.create(
        **{
            "first_name": "Hans",
            "last_name": "Peter",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "1989-03-30",
        }
    )
    assert UserBirthday.objects.count() == 1
    response = api_client.post(url, json.dumps(post_data), format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_failure_creation_of_no_required_fields(api_client):
    url = reverse("birthdays-create")
    missing_first_name = [
        {
            "first_name": "",
            "last_name": "Peter",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "30.03.1989",
        },
    ]
    missing_last_name = [
        {
            "first_name": "Hans",
            "last_name": "",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "30.03.1989",
        },
    ]
    missing_email = [
        {
            "first_name": "Hans",
            "last_name": "Peter",
            "email": "",
            "birthday": "30.03.1989",
        },
    ]
    missing_birthday = [
        {
            "first_name": "Hans",
            "last_name": "Peter",
            "email": "hanspeter@baumeister-rosing.de",
            "birthday": "",
        },
    ]
    missing_f_name_response = api_client.post(
        url, json.dumps(missing_first_name), format="json"
    )
    assert missing_f_name_response.status_code == 400

    missing_l_name_response = api_client.post(
        url, json.dumps(missing_last_name), format="json"
    )
    assert missing_l_name_response.status_code == 400

    missing_email_response = api_client.post(
        url, json.dumps(missing_email), format="json"
    )
    assert missing_email_response.status_code == 400

    missing_birthday_response = api_client.post(
        url, json.dumps(missing_birthday), format="json"
    )
    assert missing_birthday_response.status_code == 400