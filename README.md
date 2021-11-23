add app to sitting
create custom user as :

python manage.py startapp accounts
in accounts.models

class customUser(models.AbstractUser):
    email=models.EmailField(unique=True,max_length=264.verbose_name='Email Address')
    
after doing the model and adjusting the settings do the following:
python manage.py makemigrations
