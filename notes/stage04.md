## Ideation

### Draft ideas

[Research](user_based_model_research.md)

Реализовать связь ManyToMany Manager-Enterprise

При этом Manager должен обладать правами `staff` (видеть/создавать/редактировать/удалять), но с ограничениями:
- модели предприятий, с которыми он связан
- модели Driver предприятий, с которыми он связан
- модели Vehicle предприятий, с которыми он связан

Такой набор прав должен быть доступен сразу после создания нового пользователя-менеджера. -- [Кастомные permissions](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#custom-permissions)? Как запрограммировать "этот юзер может удалять модели, которые ..."?

В остальном, поля аналогичные User. Как лучше сделать: `Manager(AbstractUser)` или через `OneToOne`, как [здесь](https://stackoverflow.com/q/53920238)? -- По ТЗ, т.е. именно как наследник. Потом, если придётся создавать обычных пользователей (Employee, например), м.б. и пригодится `OneToOne` подход.


## Ход работы

1. Заготовка модели `Manager(AbstractUser)`:
  1. Удалить созданные модели из файла `vehicle_fleet/models.py`
  2. Снести файлы миграций и текущую БД.
  3. Добавить [заготовку](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) `Manager(AbstractUser)` в файл `vehicle_fleet/models.py`
  4. Задействовать кастомную модель в проекте через файл `project_root/project/settings.py`
  5. Создать и применить первую миграцию для модели `Manager(AbstractUser)`
2. Добавить в `Manager` поле по ТЗ: Enterprise (M:M), необязательное к заполнению.
3. Зарегистрировать модель в админке, настроить отображение полей.
4. Добавить в файл остальные модели.
5. Создать и применить миграции.
6. Написать файл fixtures ([пример](https://stackoverflow.com/a/60195496)) и наполнить БД.
7. Через класс `Meta` добавить набор полномочий на редактирование моделей:
  1. Как задать редактирование только определённого списка объектов Enterprise, Driver, Vehicle ??


### Шаг 1.3

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class Manager(AbstractUser):
    pass # For now we do nothinng

    def __str__(self):
        return self.username
```

### Шаг 6

Путь к файлам: `django_study_proj_03/project_root/vehicle_fleet/fixtures/enterprise.json`

Для Vehicle: пример номеров -- Р691КМ161, Е102СН102

Пример fixtures (Enterprise):
```json
[
  {
    "model": "vehicle_fleet.Enterprise",
    "pk": 1,
    "fields": {
        "title": "Abibas"
    }
  },
  {
    "model": "vehicle_fleet.Enterprise",
    "pk": 2,
    "fields": {
        "title": "Gooble"
    }
  }
]
```


## Использованные материалы

Код:
- `class AbstractBaseUser(models.Model)` -- файл `../venv/lib/python3.10/site-packages/django/contrib/auth/base_user.py`
- `class AbstractUser(AbstractBaseUser, PermissionsMixin)`, `class User(AbstractUser)` -- файл `venv/lib/python3.10/site-packages/django/contrib/auth/models.py`

## Тайминги


