from django.shortcuts import render
from django.http import HttpResponse
import shioaji as sj
from shiojia_api.app_initializer import api
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trendAccount(request):
    print(api.Contracts.Futures[a])
    return HttpResponse("OK")

def TXF1():
    contract = min(
        [
            x for x in api.Contracts.Futures.TXF 
            if x.code[-2:] not in ["R1", "R2"]
        ],
        key=lambda x: x.delivery_date
    )
    return contract

@csrf_exempt
def order(request):
    if request.method == 'POST':
        body = request.POST
        print(body.get('action'))
        if body.get('action') == 'sell':
            action = sj.constant.Action.Sell
        elif body.get('action') == 'buy':
            action = sj.constant.Action.Buy
        order_price=int(body.get('order_price'))
        quantity = int(body.get('contracts'))

        contract = TXF1()

        order = api.Order(
            action=action,
            price=order_price,
            quantity=quantity,
            price_type=sj.constant.FuturesPriceType.LMT,#{LMT: 限價, MKT: 市價, MKP: 範圍市價}
            order_type=sj.constant.OrderType.ROD, 
            octype=sj.constant.FuturesOCType.Auto,
            account=api.futopt_account
        )

        trade = api.place_order(contract, order)
        print(order)
    return HttpResponse("OK")