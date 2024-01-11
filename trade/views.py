from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shiojia_api.views import shioaji_fut_order
import shioaji as sj
import json

@csrf_exempt
def fut_order(request):
    if request.method == "POST":
        query_dict = request.POST
        data_dict = {
            'action': query_dict.get('action'),
            'price': query_dict.get('price'),
            'position_size': query_dict.get('position_size'),
            'price_type': query_dict.get('price_type')
        }
        try:
            msg = shioaji_fut_order(**data_dict)
            return JsonResponse({"status": "success", "msg": msg})
        except json.JSONDecodeError:
            # 如果請求體不是有效的 JSON，返回錯誤
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    else:
        # 如果不是 POST 請求，返回一個基本的 HTTP 回應
        return HttpResponse("Hello, world. You're at the polls index.")
