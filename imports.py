#module
import discord
import time, datetime, random, os, math, string, sys

import asyncio
import traceback
import requests

from bs4 import BeautifulSoup

import json
import html

from googleapiclient.discovery import build

import re

import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#var
DEVELOPER_KEY = os.environ["DEVELOPER_KEY"]
YOUTUBE_API_SERVICE_NAME="youtube"
YOUTUBE_API_VERSION="v3"
service = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

체크 = "✅"
엑스 = "❌"

빈공 = '​'
땀표 = '```'
공백 = ' '

도배 = True
기억 = {}      # ,기억 명령어에 사용
피버 = False   # ,피버 명령어에 사용

note = None
note2= None

지뢰 = (
    "<:0z:762919979388502027>", #0
    "<:z1:750200417836859472>", #1
    "<:z2:750200417564229673>", #2
    "<:z3:750200417304051795>", #3
    "<:z4:750200417782202429>", #4
    "<:z5:750200417421623448>", #5
    "<:z6:750200417740390442>", #6
    "<:z7:750200417748516965>", #7
    "<:z8:750200417748779059>", #8
    "<:z9:750200417417166879>", #9
    "<:z_:750200417287274529>") #10

슬롯 = ('<a:slotspin:793667557419778069>', '<a:slotseven:793668040712650783>', '<a:slotdia:793668088817123358>', '<a:slotstar:793668066692956160>', '<a:slotspade:793668129350877184>', '<a:slotheart:793668152319016980>', '<a:slotclover:793668174783709194>')

Ranks_10 = (766937626862682116, 766937654481780736, 766937674124623882, 766937691643183105, 766937708387631104)
Ranks_01 = (766937776733159424, 766937795330703390, 766937812620017665, 766937834522411028, 766938115112697866, 766938128673144833, 766938145773060096, 766938159208071188, 766938180409753601, 766938192661184522)
Tears = ('아톰', '몰레큘', '셀', '슈퍼 셀', '하이퍼 셀', '워터', '클린 워터', '아이스', '클린 아이스', '하드 아이스', '소일', '샌드', '우드', '페이퍼', '글래스', '클리어 글래스', '미러', '클리어 미러', '스톤', '하드 스톤', '아이언', '하드 아이언', '브론즈', '클리어 브론즈', '브론즈 메달', '실버', '클리어 실버', '실버 메달', '골드', '클리어 골드', '골드 메달', '클리어 크리스탈', '가넷', '아메티스트(자수정)', '아쿠아마린', '다이아몬드', '블랙 다이아몬드', '에메랄드', '문스톤', '루비', '페리도트', '사파이어')
Tears += ('오팔', '토파즈', '타코이즈(터키석)', '아다만티움', '우루', '비브라늄', '프리미엄', '딜럭스', '익스트림', '플래티넘', '미스틱', '챌린저', '마스터(티어)', '그랜드', '챔피언(티어)', '레전드')
Agains_10 = ('환생 횟수 : 0', '환생 횟수 : 1', '환생 횟수 : 2')
Agains_01 = ('0회', '1회', '2회', '3회', '4회', '5회', '6회', '7회', '8회', '9회')
God1 = ('초', '중', '고', '하', '상', '-', '+')
God2 = ('', '초하-', '초하', '초하+', '초-', '초', '초+', '초상-', '초상', '초상+', '중하-', '중하', '중하+', '중-', '중', '중+', '중상-', '중상', '중상+', '고하-', '고하', '고하+', '고-', '고', '고+', '고상-', '고상', '고상+', '초고-', '초고', '초고+')
God_Agains_10 = ('신급 환생 횟수 : 0', '신급 환생 횟수 : 1', '신급 환생 횟수 : 2', '신급 환생 횟수 : 3', '신급 환생 횟수 : 4')
God_Agains_01 = ('0회.', '1회.', '2회.', '3회.', '4회.', '5회.', '6회.', '7회.', '8회.', '9회.')

number_1 = len(Ranks_10) * len(Ranks_01) # 50
number_2 = number_1 * len(Tears) # *54
number_3 = number_2 * len(Agains_10) * len(Agains_01) # *30
number_4 =  number_3 * len(God_Agains_10) * len(God_Agains_01) # *50

#function
def 시간():
    utcnow   = datetime.datetime.utcnow()
    time_gap = datetime.timedelta(hours=9)
    kor_time = utcnow + time_gap
    n        = kor_time.strftime('%Y-%m-%d %p %I:%M:%S')
    return n

def k2e(m):
    
    배코 = 44032
    초코 = 588
    중코 = 28
    종코 = 1
    맥코 = 55203
    초성 = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    중성 = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
    종성 = ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    한글 = ('ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '')
    영어 = ('r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'E', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'Q', 'qt', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '')
    한영 = dict(zip(한글, 영어))
    영한 = dict(zip(영어, 한글))
    겹글 = "rsfqhnm"
  
    m+='.'
    f = ''
    for i in m:
        c=ord(i)
        if 배코<=c<=맥코:
            c%=배코 ; f+=한영[초성[c//초코]]
            c%=초코 ; f+=한영[중성[c//중코]]
            c%=중코 ; f+=한영[종성[c//종코]]
        else:
            try:
                f += 한영[i]
            except:
                f += i
    return f[:-1]

def e2k(m):
    
    배코 = 44032
    초코 = 588
    중코 = 28
    종코 = 1
    맥코 = 55203
    초성 = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    중성 = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
    종성 = ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    한글 = ('ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ', '')
    영어 = ('r', 'R', 'rt', 's', 'sw', 'sg', 'e', 'E', 'f', 'fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'a', 'q', 'Q', 'qt', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g', 'k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'hk', 'ho', 'hl', 'y', 'n', 'nj', 'np', 'nl', 'b', 'm', 'ml', 'l', '')
    한영 = dict(zip(한글, 영어))
    영한 = dict(zip(영어, 한글))
    겹글 = "rsfqhnm"

    m+='.'
    f=''
    w=''
    임시 = "NaN"
    #한글로 바꾸기
    for i in range(len(m)):
        if m[i] in 겹글 and len(m)>=i+2 and 임시 == "NaN":
            임시 = m[i]
        elif 임시+m[i] in 영한:
            임시 += m[i]
        elif len(임시) == 2 and 영한[m[i]] in 중성:
            w+=영한[임시[0]]
            w+=영한[임시[1]]
            w+=영한[m[i]]
            임시 = "NaN"
        elif 임시 != "NaN":
            w+=영한[임시] ; 임시 = "NaN"
            if m[i] in 겹글 and len(m)>=i+2 and 임시 == "NaN":
                임시 = m[i]
            else:
                w+=영한[m[i]] if m[i] in 영한 else m[i]
        else:
            w+=영한[m[i]] if m[i] in 영한 else m[i]
    #한글을 합치기
    w=list(w)
    임시 = []
    for i in range(len(w)):
        if len(임시) == 0:
            if w[i] in 초성:
                임시.append(w[i])
            else:
                f+=w[i]
        elif len(임시) == 1:
            if w[i] in 중성:
                임시.append(w[i])
            else:
                f+=임시[0] ; del 임시[0]
                if w[i] in 초성:
                    임시.append(w[i])
                else:
                    f+=w[i]
        else:
            if w[i] in 종성:
                if w[i] in 초성 and ((w[i+1] in 중성) if len(w)>=i+2 else False):
                    f+=chr(배코+초성.index(임시[0])*초코+중성.index(임시[1])*중코)
                    del 임시[1]
                    del 임시[0]
                    임시.append(w[i])
                else:
                    f += chr(배코 + 초성.index(임시[0])*초코 + 중성.index(임시[1])*중코 + 종성.index(w[i]))
                    del 임시[1]
                    del 임시[0]
            else:
                f+=chr(배코 + 초성.index(임시[0])*초코 + 중성.index(임시[1])*중코)
                del 임시[1]
                del 임시[0]
                if w[i] in 초성:
                    임시.append(w[i])
                else:
                    f+=w[i]
    for i in 임시:
        f+=i
    return f[:-1]
  

def translate(text):
    """
    입력된 글자가 한글이라면 영어로,
    아니라면 한글로 번역하는 코드입니다.
    네이버 파파고 api를 사용했습니다.
    """
    client_id = os.environ["translation_client_id"]
    client_secret = os.environ["translation_client_secret"]
    # 언어감지=1, 번역=2
    data1 = {'query' : text}
    url1 = "https://openapi.naver.com/v1/papago/detectLangs"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    # 먼저, 언어를 감지합니다. 
    response1 = requests.post(url1, headers=header, data=data1)
    rescode1 = response1.status_code 
    if rescode1 == 200:
        send_data1 = response1.json()
        lang_data = (send_data1['langCode'])
    else:
        lang_data = 'en'


    #언어를 감지했으므로, 번역을 합니다.
    #입력된 글자가 한글이라면 영어로,
    #아니라면 한글로 번역합니다.
    target_lang_data = 'ko' if lang_data != 'ko' else 'en'
    data2 = {'text' : text,
             'source' : lang_data,
             'target': target_lang_data}
    url2 = "https://openapi.naver.com/v1/papago/n2mt"


    response2 = requests.post(url2, headers=header, data=data2)
    rescode2 = response2.status_code

    if rescode2 == 200:
        send_data2 = response2.json()
        t_data = (send_data2['message']['result']['translatedText'])
        return t_data
    else:
        # raise Exception(f'ERROR CODE1: {rescode1}, ERROR CODE2: {rescode2}')
        return None
      
      
def get_thumbnail_by_id(id):
    thumbnails = service.videos().list(
        part = "snippet",
        id = id
    ).execute()['items'][0]['snippet']['thumbnails'].values()
    thumbnails = list(thumbnails)
    thumbnails.sort(key=lambda x: x['width'])
    return f"{thumbnails[-1]['url']}\nhttps://i.ytimg.com/vi/{id}/original.jpg"

def get_thumbnail_by_url(url):
    try_re1 = re.match(r'https://youtu[.]be/(.+)(\?.+)?', url) # 단축 url
    try_re2 = re.match(r'https://www.youtube[.]com/watch[?]v=(.+)(&.+)?', url) # 일반 url
    try_re = try_re1 or try_re2 # 둘중 match 된것

    if not try_re:
        return '올바르지 않은 url 형식입니다.'
    matched_video_id = try_re.group(1)
    return get_thumbnail_by_id(matched_video_id)

def get_last_video_by_search(search):
    channelId = service.search().list(
        q = search,
        part = "snippet",
        maxResults = 1,
        type = 'channel'
    ).execute()['items'][0]['snippet']['channelId']

    video = service.search().list(
        part = "snippet",
        channelId = channelId,
        maxResults = 1,
        type = "video",
        order = "date"
    ).execute()['items'][0]
    return f"{video['snippet']['title']}\n{get_thumbnail_by_id(video['id']['videoId'])}"
