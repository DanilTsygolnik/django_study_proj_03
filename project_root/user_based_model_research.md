## Extending the existing User model

<blockquote>

If you wish to store information related to User, you can use a `OneToOneField` to a model containing the fields for additional information. This one-to-one model is often called a profile model, as it might store non-auth related information about a site user. For example you might create an Employee model:

```python
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
```
Assuming an existing Employee Fred Smith who has both a User and Employee model, you can access the related information using Django’s standard related model conventions:

```python
>>> u = User.objects.get(username='fsmith')
>>> freds_department = u.employee.department
```

To add a profile model’s fields to the user page in the admin, define an InlineModelAdmin (for this example, we’ll use a StackedInline) in your app’s admin.py and add it to a UserAdmin class which is registered with the User class:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from my_user_profile_app.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
```

These profile models are not special in any way - they are just Django models that happen to have a one-to-one link with a user model. As such, they aren’t auto created when a user is created, but a `django.db.models.signals.post_save` could be used to create or update related models as appropriate.

Using related models results in additional queries or joins to retrieve the related data. Depending on your needs, a custom user model that includes the related fields may be your better option, however, existing relations to the default user model within your project’s apps may justify the extra database load.

-- [Extending the existing User model][1]

[1]: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model

</blockquote>

Дополнительно:
- работа в админке из под кастомного пользователя --[`django.contrib.admin`](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#custom-users-and-django-contrib-admin) 
- настройка прав кастомного пользователя -- [миксины](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#custom-users-and-permissions) 

Примеры:
- [простые вводные пояснения по AbstractUser и AbstractBaseUser](https://djangowaves.com/resources/django-user-model/) 
- https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
- https://testdriven.io/blog/django-custom-user-model/#abstractuser
- https://learndjango.com/tutorials/django-custom-user-model
- [есть листинг `AbstractUser`](https://dontrepeatyourself.org/post/django-custom-user-model-extending-abstractuser/)



## Custom User model

<blockquote>

If you’re starting a new project, it’s highly recommended to set up a custom user model, even if the default User model is sufficient for you. This model behaves identically to the default user model, but you’ll be able to customize it in the future if the need arises:

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

Don’t forget to point `AUTH_USER_MODEL` to it. Do this before creating any migrations or running `manage.py migrate` for the first time.

Also, register the model in the app’s admin.py:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

-- [Using a custom user model when starting a project][1]

[1]: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

</blockquote>

---

Referencing custom user, `AUTH_USER_MODEL`, FK -- [how to](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#referencing-the-user-model).


Примеры:
- [`AbstractBaseUser` и миксины](https://medium.com/innoventes/django-implementation-of-custom-user-management-f2ced0a19b00)

----------------------------------------------------------------

Общее время (поиски, чтение, пометки) - 3 часа
