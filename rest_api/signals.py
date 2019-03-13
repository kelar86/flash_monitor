from django.db.models.signals import post_save
from django.dispatch import receiver
from monitor.models import Problem
from .models import SearchAdvise
import json
from collections import Counter
from itertools import chain


def update_search_advise(sender, **kwargs):

    last_problems = Problem.objects.order_by('-detection_date').all()[:10]

    apps = [i + ('Application',)
            for i in last_problems.values_list('application__id', 'application__name') if i[0]]
    controls = [i + ('Control',)
                for i in last_problems.values_list('control__id', 'control__name') if i[0]]
    units = [i + ('Unit',)
             for i in last_problems.values_list('unit__id', 'unit__name') if i[0]]

    body_types = [i + ('BodyType',)
                  for i in last_problems.values_list('body_type__id', 'body_type__name') if i[0]]

    counted_list = Counter(list(chain(apps, controls, units, body_types)))

    result_list = sorted(counted_list.items(),
                         key=lambda item: item[1], reverse=True)

    result_dict = [{'id': item[0][0], 'name': item[0][1], 'type': item[0][2]}
                   for item in result_list]

    SearchAdvise.objects.update_or_create(
        pk=1, defaults={'schema': json.dumps(result_dict)})


post_save.connect(update_search_advise, sender=Problem)
