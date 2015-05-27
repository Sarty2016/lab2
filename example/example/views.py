# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from example.models import Automobile, Client, Contract


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'aaa': Automobile.objects.all(),
                'bbb': Client.objects.all(),
                'ccc': Contract.objects.all()
            }
        )
        return context


"""
Automobile.objects.create(manufacturer='FIAT', model='Punto 80 ELX', car_body='H',
                          color=u'черный', gearbox_type='M', amount=131111, engine_power=145, year=2001)
Automobile.objects.create(manufacturer='BMW', model='E94', car_body='S',
                          color=u'синий', gearbox_type='A', amount=130000, engine_power=135, year=1995)
Automobile.objects.create(manufacturer='CHEVROLET', model='Rezzo', car_body='M',
                          color=u'белый', gearbox_type='M', amount=130000, engine_power=135, year=2000)

Client.objects.create(surname=u'Иванов', patronymic=u'Иванович', name=u'Иван', gender='M', t_number='79243726800',
                      address=u'г.Неизвестный ул.Случайная д.13 кв 13',passport='7709431302',inn='121212121212')
Client.objects.create(surname=u'Иванова', patronymic=u'Ивановна', name=u'Анастасия', gender='F', t_number='79243726800',
                      address=u'г.Неизвестный ул.Случайная д 13 кв 18', passport='7709431302', inn='121212121212')
Client.objects.create(surname=u'Петров', patronymic=u'Петрович', name=u'Петр', gender='M', t_number='79243726800',
                      address=u'г.Неизвестный ул.Случайная д 13 кв 13', passport='7709431302', inn='121212121212')

Contract.objects.create(amount=130000, description='smth1',
                        auto_id=Automobile.objects.get(id=1), client_id=Client.objects.get(id=1))
Contract.objects.create(amount=131111, description='smth2',
                        auto_id=Automobile.objects.get(id=2), client_id=Client.objects.get(id=2))
Contract.objects.create(amount=130000, description='smth3',
                        auto_id=Automobile.objects.get(id=3), client_id=Client.objects.get(id=3))
"""
