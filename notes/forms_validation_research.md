# UPD: solution

Перегрузка метода:
<blockquote>

You need to define an `__init__` method for your class which should accept your product id as an argument:
```python
def __init__(self,*args,**kwargs):
    self.product_id = kwargs.pop('product_id')
    super(OrderForm,self).__init__(*args,**kwargs)
```

-- [How to request object.id in form clean data funtion][1]

[1]: https://stackoverflow.com/a/41082785

</blockquote>

Как передать `self.vehicle_id` дополнительным параметром в форму, чтобы обращаться к нему из `clean()` через `self.vehicle_id`:
<blockquote>

You need to pass it in from the view when you instantiate the form. The usual pattern is like this:

```python
class EntryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.identifier = kwargs.pop('identifier', None)
        super(EntryForm, self).__init__(*args, **kwargs)

    def clean(self):
        try:
            Entry.objects.get(
                identifier=self.identifier...
```

-- [How to pass data to clean method in Django][1]

[1]: https://stackoverflow.com/a/19144599

</blockquote>

Что ещё посмотрел, пока искал:
* [python - What to put inside __init__ method in django form class? - Stack Overflow](https://stackoverflow.com/questions/18147541/what-to-put-inside-init-method-in-django-form-class "python - What to put inside __init__ method in django form class? - Stack Overflow")
* [python - Django Queryset in ModelForm using a 'pk' - Stack Overflow](https://stackoverflow.com/questions/50691066/django-queryset-in-modelform-using-a-pk "python - Django Queryset in ModelForm using a 'pk' - Stack Overflow")
* [python - Django: Overriding __init__ for Custom Forms - Stack Overflow](https://stackoverflow.com/questions/871037/django-overriding-init-for-custom-forms "python - Django: Overriding __init__ for Custom Forms - Stack Overflow")

# Ideation

## Первая догадка (скорее всего, не то)

Нужно как-то передавать значение PK редактируемой машины в словарь значений ([dictionary mapping field names to initial values](https://stackoverflow.com/a/51463822)):
```python
form = MyForm(initial={'my_field': 'foo_bar', '<extra_field_name>': 'initial_value'})
```

---

> By default a ModelForm is dynamically created for your model. It is used to create the form presented on both the add/change pages. You can easily provide your own ModelForm to override any default form behavior on the add/change pages.     
> -- [`ModelAdmin.form`][1]

[1]: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form


## Перегрузка конструктора формы (?) -- хорошие примеры

### Пример 1

<blockquote>

You need to define an `__init__` method for your class which should accept your product id as an argument:
```python
def __init__(self,*args,**kwargs):
    self.product_id = kwargs.pop('product_id')
    super(OrderForm,self).__init__(*args,**kwargs)
```

When you initialize your form, you pass your product_id as a keyword argument.
```python
OrderForm(request.POST, product_id=product_id)
```
And in clean method you can use self.product_id to get the Product object you want.
```python
def clean_variations_select(self):
    product = Product.object.get(id=self.product_id)
    variations_select = self.cleaned_data.get("variations_select")
    if variations_select == "Variation_1" and product.variation_1 == False:
        raise forms.ValidationError("variation_1 was sold already")
    else:
        return variations_select
```

-- [How to request object.id in form clean data funtion][1]

[1]: https://stackoverflow.com/a/41082785

</blockquote>

### Пример 2

<blockquote>

Override __init__ constructor of the CustomerForm:
```python
class CustomerForm(forms.ModelForm):
    ...
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['default_tax'].queryset = 
                        fa_tax_rates.objects.filter(tenant=self.current_user))
```

Queryset in the form field definition can be safely set to all() or none():
```python
class CustomerForm(forms.ModelForm):
    default_tax = forms.ModelChoiceField(queryset=fa_tax_rates.objects.none()) 
```

-- [Django: Current User Id for ModelForm Admin][1]

<br>

[Sumup][2], `admin.py`:
```python
class MyModelForm (forms.ModelForm):

    def __init__(self, *args,**kwargs):
    super (MyModelForm ,self).__init__(*args,**kwargs)
    #retrieve current_user from MyModelAdmin
    self.fields['my_model_field'].queryset = Staff.objects.all().filter(person_name = self.current_user)

#The person name in the database must be the same as in Django User, otherwise use something like person_name__contains

class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm 

    def get_form(self, request, *args, **kwargs):
        form = super(MyModelAdmin, self).get_form(request, *args, **kwargs)
        form.current_user = request.user #get current user only accessible in MyModelAdminand pass it to MyModelForm
        return form
```

[1]: https://stackoverflow.com/a/28038666
[2]: https://stackoverflow.com/a/64813168

</blockquote>


### Пример 3

<blockquote>

```python
class ClaimRewardForm(forms.ModelForm):
    note = forms.CharField(widget=forms.Textarea)
    title = forms.ModelChoiceField(queryset=Reward.objects.all())
    # note = forms.DropDown()

    class Meta:
        model = Reward
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].queryset = Reward.objects.filter(event=self.initial['event'])
```

-- [Django: Forms Queryset][1]

[1]: https://stackoverflow.com/q/51512606

</blockquote>


### Пример 4

<blockquote>


As you know we can define a ModelForm and then replace add and change forms by setting form attribute in modelAdmin class. for example:
```python
class FooAdminForm(django.forms.ModelForm):
     class Meta:
         model = Foo

     def __init__(self, *args, **kwargs):
         super(FooAdminForm, self).__init__(self, *args, **kwargs)


class FooAdmin(admin.ModelAdmin):
    form = FooAdminForm
```
in a simple view we can initialize a form object and pass extra arguments to init function of the form. something like this:
```python
def my_view(request):
    form = FooAdminForm(p1='aaa', p2='bbb')
```
and then in the init function we can access these parameter.
```python
self.p1 = kwargs.pop('p1')
self.p2 = kwargs.pop('p2')
```

-- [Suggestion][1]


... if you're using a custom form, you can simply pass it to super().get_form() using kwargs
```python
def get_form(self, request, obj=None, **kwargs):
    kwargs['form'] = FooAdminForm
    Form = super().get_form(request, obj=None, **kwargs)
    return functools.partial(Form, user=request.user)
```

-- [Better solution ??][2]



[1]: https://stackoverflow.com/q/38811627
[2]: https://stackoverflow.com/a/64653941

</blockquote>


## Перегрузка конструктора формы (?) -- прочие примеры

<blockquote>

```python
class MyAdmin(admin.ModelAdmin):
    form = MyForm

    def get_form(self, request, **kwargs):
        form = super(MyAdmin, self).get_form(request, **kwargs)
        form.current_user = request.user
        return form

# Моё предпололжение исходя из подсказки
class MyForm(forms.ModelForm):
    def __init__(self, author, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.author = author
        # access to current user by self.current_user
```

-- [Ветка: Use a form with a custom `__init__` in Django Admin][1]     
-- [Подсказка][2]

[1]: https://stackoverflow.com/questions/26959934/use-a-form-with-a-custom-init-in-django-admin
[2]: https://stackoverflow.com/a/26962459

</blockquote>



<blockquote>

```python
class SpacecraftID(forms.Form):

    def __init__(self,*args,**kwargs):
        choices = kwargs.pop('choices')
        super(SpacecraftID,self).__init__(*args,**kwargs)

        # Set choices from argument.
        self.fields['scId'].choices = choices

    # Set choices to an empty list as it is a required argument.
    scID = forms.MultipleChoiceField(
        required=False, 
        widget=forms.CheckboxSelectMultiple, 
        choices=[]
    )
```

-- [Django: how to pass parameters to forms][1]

[1]: https://stackoverflow.com/a/29974309

</blockquote>
