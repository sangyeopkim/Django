import json
import os

from pip._vendor import requests


current_file_path = os.path.abspath(__file__)
print(current_file_path)

# 현재 파일에서 한 단계 부모 디렉토리(youtube/code)
go_to_parent_path1 = os.path.dirname(current_file_path)
print(go_to_parent_path1)

# code 디렉토리 보다 한 단계 위, 즉 현재 파이참 프로젝트 루트 폴더(youtube)
go_to_parent_path2 = os.path.dirname(go_to_parent_path1)
print(go_to_parent_path2)

# 루트 폴더의 바로 아래 .conf폴더(youtube/.conf)
path_dir_conf = os.path.join(go_to_parent_path2, '.conf')
print(path_dir_conf)

# .conf 폴더 내부의 settings_local.json 파일
path_file_settings_local = os.path.join(path_dir_conf, 'settings_local.json')
print(path_file_settings_local)

# 파일을 열고 읽는다
f = open(path_file_settings_local, 'r')
config_str = f.read()
f.close()

config = json.loads(config_str)

print(config_str)
print(config)

# API_KEY 가져오
youtube_api_key = config['youtube']['API_KEY']
print(youtube_api_key)

params = {
    'part': 'snippet',
    'q': '한지민',
    'maxResults': 30,
    'key': youtube_api_key
}
r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
result = r.text
result_dict = json.loads(result)

kind = result_dict['kind']
etag = result_dict['etag']
next_page_token = result_dict['nextPageToken']
region_code = result_dict['regionCode']
page_info = result_dict['pageInfo']
page_info_total_results_per_page = page_info['totalResults']
page_info_results_per_page = page_info['resultsPerPage']

print('kind: %s' % kind)
print('etag: %s' % etag)
print('next_page_token: %s' % next_page_token)
print('region_code : %s' % region_code)
print('page_info_total_results_per_page : %s' % page_info_total_results_per_page)
print('page_info_results_per_page : %s' % page_info_results_per_page)

items = result_dict['items']
for index, item in enumerate(items):
    title = item['snippet']['title']
    published_date = item['snippet']['publishedAt']
    print(index, title)
    print(published_date)
