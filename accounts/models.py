from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザー",max_length=30)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=6)
    city = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=200)



from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
 
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
 
class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
 
    is_active = models.BooleanField(default=True)
 
    is_admin = models.BooleanField(default=False)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
 
    REQUIRED_FIELDS = []
 
    def __str__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# --- OneToOneField を同時に作成 ---

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_onetoone(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
# --- OneToOneField を同時に作成 ---


