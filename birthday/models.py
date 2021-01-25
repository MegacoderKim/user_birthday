from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserBirthday(models.Model):
    first_name = models.CharField(
        _("First Name"), max_length=200, null=False, blank=False
    )
    last_name = models.CharField(
        _("Last Name"), max_length=200, null=False, blank=False
    )
    email = models.EmailField(_("Email"), unique=True, null=False, blank=False)
    birthday = models.DateField(_("Birthday"), null=False, blank=False)

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.birthday.year
            - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
