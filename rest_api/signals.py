from django.db.models.signals import post_save
from django.dispatch import receiver
from monitor.models import Problem
from .models import SearchAdvise
import json

# import logging
# logger = logging.getLogger(__name__)


@receiver(post_save, sender=Problem)
def update_search_advise(sender, **kwargs):

    # logger.error('SIGNAL!!!')

    last_problems = Problem.objects.all()[:10]

    apps = [i + ('application',)
            for i in last_problems.values_list('application__id', 'application__name') if i[0]]
    controls = [i + ('control',)
                for i in last_problems.values_list('control__id', 'control__name') if i[0]]
    units = [i + ('unit',)
             for i in last_problems.values_list('unit__id', 'unit__name') if i[0]]

    counted_list = Counter(list(chain(apps, controls, units)))

    result_list = sorted(counted_list.items(),
                         key=lambda item: item[1], reverse=True)

    result_dict = [{'id': item[0][0], 'name': item[0][1], 'type': item[0][2]}
                   for item in result]

    SearchAdvise.objects.update_or_create(
        pk=1, defaults={'schema': json.dumps(result_dict)})
