from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
  """Helps working with costume user model"""

  def create_user(self, email, name, password=None):
    """Creates a new user profile object"""

    # Checks if email is entered
    if not email:
      raise ValueError('Email adress is required.')

    email = self.normalize_email(email) # Normalizes email and creates new object
    user = self.model(email=email, name=name)

    # Hides a password
    user.set_password(password)
    user.save(using=self._db)

    return user


  def create_superuser(self, email, name, password):
    """Creates a new superuser"""

    user = self.create_user(email, name, password)

    # Make this user an admin.
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Represents user profile in our system"""

  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)  # Determins if user is currently active in system
  is_staff = models.BooleanField(default=False)

  object = UserProfileManager()

  USERNAME_FIELD = 'email'
  # List of required fields
  REQUIRED_FIELDS = ['name']


  def get_full_name(self):
    """Gets user full name"""

    return self.name

  def get_short_name(self):
    """"Gets users short name"""

    return self.name


  def __str__(self):
    """"Represents object as a string"""

    return self.email


class ProfileFeedItem(models.Model):
  """Profile status update"""

  user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
  status_text = models.CharField(max_length=255)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return model as a string"""

    return self.status_text