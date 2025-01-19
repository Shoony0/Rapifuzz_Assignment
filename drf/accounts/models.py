from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser
from django.utils.translation import gettext_lazy as _


LOGIN_TYPE = (
    (0, "Individual"),
    (1, "Enterprise"),
    (2, "Goverment"),
)
INCIDENT_PRIORITY = (
    (0, "Low"),
    (1, "Medium"),
    (2, "High"),
)
INCIDENT_STATUS = (
    (0, "Open"),
    (1, "In progress"),
    (2, "Closed"),
)


class CustomUserManager(models.Manager):
    def get_by_natural_key(self, email):
        return self.get(email=email)
    
class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    login_type = models.SmallIntegerField(_("login_type"), choices=LOGIN_TYPE, default=0)
    address = models.TextField(_("address"), null=True, blank=True)
    country = models.CharField(_("country"), max_length=30, null=True, blank=True)
    state = models.CharField(_("state"), max_length=30, null=True, blank=True)
    city = models.CharField(_("city"), max_length=30, null=True, blank=True)
    pincode = models.CharField(_("pincode"), max_length=10, null=True, blank=True)
    mobile_number_code = models.CharField(_("mobile_number_code"), max_length=5, null=True, blank=True)
    mobile_number = models.CharField(_("mobile_number"), max_length=10, null=True, blank=True)
    fax = models.CharField(_("fax"), max_length=20, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self) -> str:
        return super().get_full_name()


class Incident(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=12, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.SmallIntegerField(choices=INCIDENT_PRIORITY, default=0)
    details = models.TextField()
    status = models.SmallIntegerField(choices=INCIDENT_STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
