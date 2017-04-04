import json

import requests
from django.shortcuts import render

from utils.settings import get_settings


def get_search_list_from_google(keyword):
    google_map_api_key = get_settings()['google_map']['API_KEY']
    params = {
        'key': google_map_api_key,
        'query': keyword,
    }
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?parameters', params=params)
    result = r.text
    result_dict = json.loads(result)

    results = result_dict['results']
    return results


def search(request):
    places = []

    keyword = request.GET.get('keyword', '').strip()
    if keyword != '':
        results = get_search_list_from_google(keyword)

        for result in results:
            formatted_address = result['formatted_address']

            cur_item_dict = {
                'formatted_address': formatted_address,
            }
            places.append(cur_item_dict)
    context = {
        'places': places,
    }
    return render(request, 'places/search.html', context)
