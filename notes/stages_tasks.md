## Этап 1

Создать основную модель Vehicle (автомобиль) с несколькими полями на усмотрение (например, стоимость, год выпуска, пробег, и т. д.). Марку/бренд с техническими характеристиками пока не добавлять - это будет отдельная модель.

Зарегистрировать модель в админке, добавить 3-5 объектов в базу.


## Этап 2

Добавить отдельную модель брендов и привязать её к модели Vehicle, чтобы в админке, когда создаётся или редактируется новый автомобиль, поле бренда показывалось как выпадающий список. 

Добавить в модель Vehicle несколько других характеристик (например, тип авто, кол-во мест, цвет).

Выводить данные автомобиля в админке в более наглядном виде: id + бренд + пробег или цена например.


## Этап 3

Добавить ещё две базовые модели:
1. Enterprise (предприятие)
2. Driver (водитель)

    Основные поля этим моделям придумать самостоятельно. Например, название + город, имя + зарплата.

    Организовать между ними такие связи:
    - Предприятию могут принадлежать несколько автомобилей (один ко многим).
    - Предприятию могут принадлежать несколько водителей (один ко многим).

    Дополнительные условия:
    - Автомобиль и водитель могут принадлежать только одному предприятию.
    - Каждому автомобилю может быть назначено несколько водителей (один к многим).
    - Один из назначенных водителей дополнительно считается "активным" (флажок) — это тот, кто работает на машине в данный момент.
    - Создаваемый водитель исходно ни к какой машине не привязан.
    - Автомобиль может переназначаться в админке другому предприятию, только если для него не назначен водитель (с галкой).

## Этап 4

Добавить модель Manager (менеджер), наследник от User (менеджер авторизовывается в админке как обычный user).

Предприятию могут принадлежать несколько менеджеров.

Менеджеру могут "принадлежать" (быть видимыми) несколько предприятий.

Менеджер может видеть/создавать/редактировать/удалять автомобили и водителей только в видимых ему предприятиях.

Сделать случай, когда три предприятия 1,2,3 и два менеджера, одному принадлежат предприятия 1,2, другому 2,3.
