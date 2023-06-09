from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
)

class AccountManager(BaseUserManager):
	def _create_user(self, email, username, password, **extra_field):
		if not email:
			raise ValueError(_('No email provided.'))
		if not username:
			raise ValueError(_('No username provided.'))
		
		user = self.model(
			email = self.normalize_email(email),
			username = username,
			**extra_field,
		)
		user.set_password(password)
		user.save(using=self._db)

		return user
	
	def create_user(self, email=None, username=None, password=None, **extra_field):
		extra_field.setdefault('is_staff', False)
		extra_field.setdefault('is_admin', False)
		extra_field.setdefault('is_superuser', False)
		extra_field.setdefault('is_active', False)

		return self._create_user(email, username, password, **extra_field)

	def create_superuser(self, email=None, username=None, password=None, **extra_field):
		extra_field.setdefault('is_staff', True)
		extra_field.setdefault('is_admin', True)
		extra_field.setdefault('is_superuser', True)
		extra_field.setdefault('is_hotel_manager', True)

		return self._create_user(email, username, password, **extra_field)
	
def get_profile_image_path(self, filename):
	return f'static/profile_images/{self.pk}/{filename}'

def get_default_profile_image():
	return "static/default.png"

class Account(
	TimeStampedModel, 
	ActivatorModel,
	AbstractUser,
	PermissionsMixin,
):
	
	class Meta:
		verbose_name = "Account"
		verbose_name_plural = "Accounts"

		permissions = [
			("is_hotel_manager", "can manage reservation")
		]

	username = models.CharField(max_length=50, default="new user")
	email = models.EmailField(verbose_name="Email", unique=True, blank=True)
	phone_number = models.CharField(max_length=11, blank=True)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_hotel_manager = models.BooleanField(default=False)

	profile_image = models.ImageField(
		max_length=255, 
		upload_to=get_profile_image_path, 
		null=True,
		blank=True,
		default=get_default_profile_image
	)

	USERNAME_FIELD = "email"
	EMAIL_FIELD = "email"
	REQUIRED_FIELDS = ["username"]

	objects = AccountManager()

	def __str__(self):
		return f'{self.username}'
	
	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/')]

	def has_perm(self, perm: str, obj= None) -> bool:
		return self.is_staff
	
	def has_module_perms(self, app_label: str) -> bool:
		return True
