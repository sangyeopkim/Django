import json

import requests
from dateutil.parser import parse
from django.shortcuts import render

from utils.settings import get_settings
from video.models import Video


def get_search_list_from_youtube(keyword):
    youtube_api_key = get_settings()['youtube']['API_KEY']
    params = {
        'part': 'snippet',
        'q': keyword,
        'maxResults': 30,
        'type': 'video',
        'key': youtube_api_key,
    }
    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    result = r.text
    result_dict = json.loads(result)

    items = result_dict['items']
    return items


def search(request):
    # 검색결과를 담을 리스트
    videos = []
    # GET parameters에 keyword값이 왔을때만 검색결과에 내용이 추가됨
    keyword = request.GET.get('keyword', '').strip()
    if keyword != '':
        items = get_search_list_from_youtube(keyword)

        for item in items:
            published_date_str = item['snippet']['publishedAt']

            # 실제로 사용할 데이터
            youtube_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            published_date = parse(published_date_str)
            url_thumbnail = item['snippet']['thumbnails']['high']['url']

            # 현재 item을 dict로 정리
            cur_item_dict = {
                'title': title,
                'description': description,
                'published_date': published_date,
                'youtube_id': youtube_id,
                'url_thumbnail': url_thumbnail,
            }
            videos.append(cur_item_dict)
    context = {
        'videos': videos,
    }
    return render(request, 'video/search.html', context)
