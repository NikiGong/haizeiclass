from django.shortcuts import render
from interface_main.utils.http_format import response_success,response_failed
from interface_main.utils.log import default_log
from interface_main.exception.my_exception import MyException

# Create your views here.

def test_success(request):
    a=2
    b=2
    c=2

    if a!=1:
        print("hahahahha")
        raise MyException(message="aaaaa")   # 抛出异常，会去到中间件my_middle_ware.py的process_exception里面，来判断是什么异常
    # default_log.info("info-1")
    return response_success({"a" : 1})


def test_failed(request):
    # default_log.log("error-1")
    return response_failed(10000, "普通错误")

# def func():
#     raise  Exception('')