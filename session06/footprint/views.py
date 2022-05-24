from django.shortcuts import render

from footprint.models import Footprint
from django.http import JsonResponse
import json


def footprint_GET(request):
    footprints = Footprint.objects.filter(receiver='강민지').order_by('-sent_at')
    messages = []

    for i in range(len(footprints)):
        messages.append(footprints[i].message)
    # 메세지가 전송된 순서대로 가져오라는 뜻. order_by('sent_at')

    return JsonResponse({
        'status': 200,
        'message': 'Footprint 조회 성공',
        'data': {
            'messages': messages,
            }
    })
# 2줄 씩 띄워야 됨!

def footprint_POST(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    Footprint.objects.create(message=body['content'], receiver=body['receiverName'])

    return JsonResponse({
        'status': 200,
        'message': '메세지 전송 성공'
    })

# Create your views here.
