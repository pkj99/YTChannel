import requests
import os
# import sys

txt = '#EXTM3U url-tvg="http://epg.51zmt.top:8000/e.xml"'

# windows = False
# if 'win' in sys.platform:
#     windows = True

def grab(url):
    global txt
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            # if windows:
            #     # print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
            #     txt += '\nhttps://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
            #     return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                # print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                txt += '\nhttps://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    # print(f"{link[start : end]}")
    txt += f"\n{link[start : end]}\n"

# print('#EXTM3U url-tvg="http://epg.51zmt.top:8000/e.xml"')

# with open('youtube_channel_info.txt', encoding='utf-8') as f:
with open('youtube_channel_info.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            # print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
            txt += f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}'
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.remove("temp.txt")
    # os.system('del temp.txt')


f = open('youtube.m3u','w',encoding='utf-8')
f.write(txt)
f.close