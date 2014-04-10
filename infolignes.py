#!/usr/bin/env python

import logging
import datetime
import time

import requests
from lxml import html


logging.basicConfig()
logger = logging.getLogger('infolignes')
logger.setLevel(logging.DEBUG)


def get_next_trains(city_source, city_dest):
    departure_date = datetime.date.today()
    payload = {}
    payload['cityDepart'] = city_source
    payload['cityDestination'] = city_dest
    payload['date_num_train'] = departure_date.strftime('%Y|%m|%d')
    payload['train_horaire_depart'] = time.strftime('%H|%M')
    payload['type_heure'] = 1
    r = requests.get('http://www.infolignes.com/recherche.php', params=payload)
    logger.info('Fetching {}'.format(r.url))
    tree = html.fromstring(r.text)
    results = tree.xpath('//table[@class="resultat"]')
    for result in results:
        steps = result.xpath('//tbody/tr')
        direct = len(steps) == 1
        logger.info('Direct={}'.format(direct))
        for step in steps:
            cols = step.xpath('//td/text()', smart_strings=False)
            cols = [col.strip() for col in cols]
            print(cols)

if __name__ == '__main__':
    get_next_trains(city_source=76540, city_dest=75056)
    print('')
    get_next_trains(city_source=75056, city_dest=76540)
