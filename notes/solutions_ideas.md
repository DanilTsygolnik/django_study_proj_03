## Choices в Vehicle

**Идея**: заменить реализацию выпадающих списков в админке через модели.

Решение:  [^admin-editing-model-drop-down-menus-choices]
1. Написать кастомную форму для редактирования модели Vehicle в админке -- forms.py
2. Добавить поля под соответствующие поля модели:
```python
from django import forms


# Choices for the form
VEHICLE_COLOR_CHOICES = [
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('green', 'Green'),
]

class VehicleForm(forms.Form):
    vehicle_color = forms.ChoiceField(choices=VEHICLE_COLOR_CHOICES)
```



Что хочу видеть в админке по модели Vehicle
название в формате "Brand Model license-plate-number"
пробег
компания-владелец
свободна (поле из админки, динамически на основе активного водилы)


## Меняем владельца тачки только если она неактивна

Идея:
- добавить в форму админки для модели Vehicle поле "Is busy": true - у машины есть водитель со статусом `is_driving=True`, false - в противном случае.  [^django-model-custom-fields-for-the-admin]
- в поле "Vehicle owner" (`Vehicle.owner` в модели) можно выбирать компанию (связанная модель Enterprise). Добавить кастомную валидацию этого поля:
    - при сохранении на экран выводится сообщение "Нельзя переназначить предприятие - Vehicle is busy. Нужно изменить статус `is_driving` у водителя X"
    - значение сбрасывалется до уже имеющегося в модели


Кастомный валидатор с сообщением:
```python
class Vehicle(models.Model):
    owner = models.ForeignKey(Enterprise, on_delete=models.SET_NULL)

    def clean(self):
        vehicle_is_busy = 
        self.owner
        if vehicle_is_busy:
            raise ValidationError(
                "Нельзя переназначить предприятие - Vehicle is busy. \
                Нужно изменить статус `is_driving` у водителя X"
            )
```

Кастомный валидатор со сбросом значения поля owner:   [^django-admin-make-field-editable-on-condition]
```python
# admin.py
# define your own form for the admin
# custom validate 'owner' field, rejecting if it is already set

class VehicleAdminForm(forms.ModelForm):
    class Meta:
        model = Vehicle

    def clean_third_party_id(self):
        # отображение Enterprise.title


        cleaned_data = self.cleaned_data
        third_party_id = cleaned_data['third_party_id']
        id = cleaned_data['id']
        obj = Product.objects.get(id=id)
        if obj.third_party_id != third_party_id:
            raise ValidationError(
                _(
                    "You cannot change the owner until the vehicle is busy.\n \
                    Change 'is_driving' field for the driver %(driver_id)s \
                    first."
                ),
                code='changing_vehicle_owner_while_busy',
                params={'driver_id': ?? },
         return third_party_id


class ProductAdmin(admin.Admin):
    form = [ProductAdminForm,]
```


## tbs


[How to show many to many or reverse FK fields on listview page?](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/many_to_many.html). 


### Editable model fields in the admin on condition


- [python - how to show a django ModelForm field as uneditable - Stack Overflow](https://stackoverflow.com/questions/7088321/how-to-show-a-django-modelform-field-as-uneditable "python - how to show a django ModelForm field as uneditable - Stack Overflow")
- [python - conditional editing in django model - Stack Overflow](https://stackoverflow.com/questions/61039438/conditional-editing-in-django-model "python - conditional editing in django model - Stack Overflow")
- [python - Django Admin- disable Editing and remove "Save" buttons for a specific model - Stack Overflow](https://stackoverflow.com/questions/8442724/django-admin-disable-editing-and-remove-save-buttons-for-a-specific-model "python - Django Admin- disable Editing and remove "Save" buttons for a specific model - Stack Overflow")
- [Django admin: make field editable in add but not edit - Stack Overflow](https://stackoverflow.com/questions/7860612/django-admin-make-field-editable-in-add-but-not-edit "Django admin: make field editable in add but not edit - Stack Overflow")
- [python 3.x - make some model field conditionally visible in django - Stack Overflow](https://stackoverflow.com/questions/49870881/make-some-model-field-conditionally-visible-in-django "python 3.x - make some model field conditionally visible in django - Stack Overflow")
- [Django ModelForm and Conditionally Disabled (Readonly) Fields – Ramblings on startups, NYC, advertising and hacking (mostly Python)](https://chriskief.com/2013/09/28/django-modelform-and-conditionally-disabled-readonly-fields/ "Django ModelForm and Conditionally Disabled (Readonly) Fields – Ramblings on startups, NYC, advertising and hacking (mostly Python)")
- [python - make django model field read only or disable in admin while saving the object first time - Stack Overflow](https://stackoverflow.com/questions/28275239/make-django-model-field-read-only-or-disable-in-admin-while-saving-the-object-fi "python - make django model field read only or disable in admin while saving the object first time - Stack Overflow")



Добавить в форму редактирования модели кастомное read-only поле  [^write-a-read-only-widget-and-specify-it-directly-on-your-form]
Задать в виджете [^set-form-widget-initial-value] dynamically generated значение (true/false) -- это же значение использовать для валидации 

<quoteblock>
<a href="https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form">ModelAdmin.form</a>
    
By default a ModelForm is dynamically created for your model. It is used to create the form presented on both the add/change pages. You can easily provide your own ModelForm to override any default form behavior on the add/change pages. Alternatively, you can customize the default form rather than specifying an entirely new one by using the <a href="https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_form">ModelAdmin.get_form()</a> method.
    
For an example see the section <a href="https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#admin-custom-validation">Adding custom validation to the admin</a>.
</quoteblock>




[^admin-editing-model-drop-down-menus-choices]: resourses
  - [choices](https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets) -- см. DateField (виджеты) и ChoicesField.
[^write-a-read-only-widget-and-specify-it-directly-on-your-form]: resourses
  - widget -- https://stackoverflow.com/a/15347196
  - add custom field example -- https://stackoverflow.com/a/29057206
[^set-form-widget-initial-value]: https://stackoverflow.com/a/604325
[^django-model-custom-fields-for-the-admin]: resourses
  - [example 1](https://stackoverflow.com/a/9166179) 
[^django-admin-make-field-editable-on-condition]: https://stackoverflow.com/a/7860791

