from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shiojia_api.app_initializer import api

import json
import shioaji as sj



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trendAccount(request):
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

def get_positions(request):
    positions = api.list_positions(api.futopt_account)
    list = []
    for p in positions:
        list.append({"code":p.code,"quantity":p.quantity,"direction":p.direction})
    print(positions)
    return JsonResponse({"status": "success", "positions": list})
def find_contract(code):
    positions = api.list_positions(api.futopt_account)
    for position in positions:
        if position.code == code:
            print(position)
            return position

def shioaji_fut_order(action,price,position_size,octupy="Auto",price_type="LMT",order_type="ROD"):
    contract = TXF1()
    position = find_contract(contract.code)
    if position:

        if position.direction == sj.constant.Action.Sell:
            if action == "Buy":
                quantity = position.quantity + abs(int(position_size))
            if action == "Sell":
                quantity = abs(int(position_size)) - position.quantity
        elif position.direction == sj.constant.Action.Buy:
            if action == "Sell":
                quantity = position.quantity + abs(int(position_size))
            if action == "Buy":
                quantity = abs(int(position_size)) - position.quantity
        
        if quantity > 0:
            order = api.Order(
                action=sj.constant.Action[action],
                price=int(price),
                quantity=abs(int(quantity)),
                price_type=sj.constant.FuturesPriceType[price_type],#{LMT: 限價, MKT: 市價, MKP: 範圍市價}
                order_type=sj.constant.OrderType[order_type], 
                octype=sj.constant.FuturesOCType[octupy],
                account=api.futopt_account
            )
            trade = api.place_order(contract, order)
            return "下單成工"
        else:
            return "不符合"
    else:
        order = api.Order(
            action=sj.constant.Action[action],
            price=int(price),
            quantity=abs(int(position_size)),
            price_type=sj.constant.FuturesPriceType[price_type],#{LMT: 限價, MKT: 市價, MKP: 範圍市價}
            order_type=sj.constant.OrderType[order_type], 
            octype=sj.constant.FuturesOCType[octupy],
            account=api.futopt_account
        )
        trade = api.place_order(contract, order)
        return "下單成工"

    # order = api.Order(
    #     action=sj.constant.Action[action],
    #     price=int(price),
    #     quantity=int(quantity),
    #     price_type=sj.constant.FuturesPriceType[price_type],#{LMT: 限價, MKT: 市價, MKP: 範圍市價}
    #     order_type=sj.constant.OrderType[order_type], 
    #     octype=sj.constant.FuturesOCType[octupy],
    #     account=api.futopt_account
    # )
    # print(order)
    # trade = api.place_order(contract, order)
    return HttpResponse("OK")