from django.core.management.base import BaseCommand
from educenterapp.models import Person, Group, Subject, Lesson, Result
import datetime, random

class Command(BaseCommand):

    def handle(self, *args, **options):
        # очищаем данные из базы
        Subject.objects.all().delete()
        Group.objects.all().delete()
        Person.objects.all().delete()
        Lesson.objects.all().delete()
        Result.objects.all().delete()

        #заполняем таблицу предметов
        subj_list = [
            'Физика',
            'Математика',
            'История'
        ]
        print('Предметы')
        for item in subj_list:
            Subject.objects.create(name=item)
            newitem  = Subject.objects.get(name=item)
            print(f'{newitem.id} {newitem.name}')

        #проверка заполненных данных
        #способ 1
        subj_list = list(Subject.objects.all().values_list('id', flat=True))
        print(subj_list)
        # способ 2
        subj_list1 = Subject.objects.in_bulk().keys()
        print(subj_list1)

        now = datetime.datetime.now().date()

        # Заполняем таблицу персон
        pers_list = [
            'Иванов Иван',
            'Петров Петр',
            'Сидоров Сидор'
        ]
        print('Персоны')

        for item in pers_list:
            Person.objects.create(name=item, bday=now)
            newitem  = Person.objects.get(name=item)
            print(f'{newitem.id} {newitem.name}')

        #проверка заполненных данных
        pers_list = list(Person.objects.all().values_list('id', flat=True))
        print(pers_list)

        # Заполняем таблицу учебных групп
        group_list = [
            '1_класс',
            '2_класс',
            '3_класс'
        ]
        print('Группы')

        for item in group_list:
            Group.objects.create(name=item)
            newitem  = Group.objects.get(name=item)
            print(f'{newitem.id} {newitem.name}')

        #проверка заполненных данных
        gro_list = list(Group.objects.all().values_list('id', flat=True))
        print(gro_list)


        # заполняем таблицу уроков
        less_list = [
            '0_Введение',
            '1_урок',
            '2_урок'
        ]
        print('Уроки')
        # уроки (класс и предмет) создаем случайным образом
        for item in less_list:
            Lesson.objects.create(name=item,
                                  group_id=random.choice(gro_list),
                                  subject_id=random.choice(subj_list))
            newitem = Lesson.objects.get(name=item)
            print(f'{newitem.id} {newitem.name}')

        #проверка заполненных данных
        less_list = list(Lesson.objects.all().values_list('id', flat=True))
        print(less_list)

        less = Lesson.objects.all()
        print(less)
        for les in less:
            print(les)
            print(les.name, les.group_id, les.subject_id)

        # заполняем таблицу экзаменов
        res_list = [
            'Тестирование',
            'Контрольная',
            'Экзамен'
        ]
        print('Результаты')

        for item in res_list:
            for item_g in gro_list:
                for item_l in less_list:
                    for item_p in pers_list:
                        for item_s in subj_list:
                            # в таблицу случайным образом заносим один из 10 результатов
                            if (random.randint(0,100) % 10) == 0:
                                Result.objects.create(date=now,
                                    mark=random.randint(3,5),
                                    group_id=item_g,
                                    lesson_id=item_l,
                                    person_id=item_p,
                                    subject_id=item_s)
        newitem = Result.objects.all().values_list()
        print(newitem)

        # проверочная печать
        print('БД заполнена данными')


