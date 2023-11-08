import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Notice

def mainpage(request):
    return render(request, 'userpage/userpage.html')

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',

        # 키워드 버튼 추가
        'buttons':['키워드1','키워드2',]
    })

def message(request):

    message = ((request.body).decode('utf-8'))
    request_data = json.loads(message)

    # 유저로부터 온 응답 메세지
    userMessage = request_data['content']
    # 유저로부터 온 응답메세지 타입
    userType = request_data['type']

    if userMessage == '키워드1':
        return JsonResponse({
            'message':{
                'text': '키워드1에 대한 답변',
                'photo':{
                    'url': '',
                    'width':640,
                    'height': 480
                },
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['키워드1','키워드2']
            }
        })