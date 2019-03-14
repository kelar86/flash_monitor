from django.db.models.signals import post_save
from django.dispatch import receiver
from monitor.models import Problem
from .models import SearchAdvise
import json
from collections import Counter
from itertools import chain
from django.conf import settings


def update_search_advise(sender, **kwargs):

    last_problems = Problem.objects.order_by('-detection_date').all()[:10]

    apps = [('Application',) + i
            for i in last_problems.values_list('application__id', 'application__name', 'application__icon') if i[0]]
    controls = [('Control',) + i
                for i in last_problems.values_list('control__id', 'control__name', 'control__icon') if i[0]]
    units = [('Unit',) + i
             for i in last_problems.values_list('unit__id', 'unit__name', 'unit__icon') if i[0]]

    body_types = [('BodyType',) + i
                  for i in last_problems.values_list('body_type__id', 'body_type__name', 'body_type__icon') if i[0]]

    counted_list = Counter(list(chain(apps, controls, units, body_types)))

    result_list = sorted(counted_list.items(),
                         key=lambda item: item[1], reverse=True)

    result_dict = [{'type': item[0][0], 'id': item[0][1], 'name': item[0][2], 'icon': '' + settings.BASE_URL + settings.MEDIA_URL + item[0][3]}
                   for item in result_list]

    SearchAdvise.objects.update_or_create(
        pk=1, defaults={'schema': json.dumps(result_dict)})


post_save.connect(update_search_advise, sender=Problem)
