import json

import requests
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from utils.settings import get_settings
from video.models import Video


def search_from_youtube(keyword, page_token=None):
    youtube_api_key = get_settings()['youtube']['API_KEY']
    params = {
        'part': 'snippet',
        'q': keyword,
        'maxResults': 10,
        'type': 'video',
        'key': youtube_api_key,
    }
    # 페이지 토큰값이 전달되었을 때만 params에 해당 내용을 추가해서 요
    if page_token:
        params['pageToken'] = page_token
    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    result = r.text
    result_dict = json.loads(result)
    return result_dict


def search(request):
    # 검색결과를 담을 리스트
    videos = []
    context = {
        'videos': videos
    }

    # GET parameters에 keyword값이 왔을때만 검색결과에 내용이 추가됨
    keyword = request.GET.get('keyword', '').strip()
    page_token = request.GET.get('page_token')

    if keyword != '':
        # 검색 결과를 받아옴
        search_result = search_from_youtube(keyword, page_token)

        # 검색결과에서 이전/다음 토큰, 전체 결과 개수를 가져와
        # 템플릿에 전달할 context 객체에 할당
        next_page_token = search_result.get('nextPageToken')
        prev_page_token = search_result.get('prevPageToken')
        total_results = search_result['pageInfo'].get('totalResults')
        items = search_result['items']
        context['next_page_token'] = next_page_token
        context['prev_page_token'] = prev_page_token
        context['total_results'] = total_results
        context['keyword'] = keyword

        # 검색 결과에서 'items' 키를 갖는 list를 items 변수에 할당 후 loop
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
    return render(request, 'video/search.html', context)


@login_required
def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        youtube_id = request.POST['youtube_id']
        published_date_str = request.POST['published_date']
        published_date = parse(published_date_str)
        prev_path = request.POST['path']

        defaults = {
            'title': title,
            'description': description,
            'published_date': published_date,
        }
        video, _ = Video.objects.get_or_create(
            defaults=defaults,
            youtube_id=youtube_id
        )
        request.user.bookmark_videos.add(video)
        return redirect(prev_path)

