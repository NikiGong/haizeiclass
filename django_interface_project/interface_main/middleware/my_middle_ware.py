import traceback  # 用来打印异常
# import django.core.exceptions  # django自己的异常
from django.db import DatabaseError
from django.utils.deprecation import MiddlewareMixin
from interface_main.utils.http_format import response_success, response_failed
from interface_main.exception.my_exception import MyException, ErrorCode

# 中间件：是用来做统一的异常处理，(这里的中间件是指django里面的中间件，在settings.py里面注册就可以)

class MyMiddleWare(MiddlewareMixin):  # 继承MiddlewareMixin，重写process_request、process_response、process_exception
    def process_request(self,request):  # 会捕捉所有的请求
        # print("请求进来了")
        pass

    def process_response(self, request, response):  # 会捕捉所有的响应
        # print("响应来了")
        return response  # 一定要有的

    def process_exception(self, request, exception):  # 会捕捉到所有的异常
        # print("捕捉到异常")
        code = exception.code
        message = exception.message
        # return response_failed()
        print(traceback.print_exc())  # 打印异常，调用该方法只要有异常都会打印
        # 用来isinstance()专门用来判断对象的类型
        if isinstance(exception, MyException):  # 用来判断异常类型是否是MyException
            print("这是我的错误")
            return response_failed(exception.message)

        elif isinstance(exception, DatabaseError):  # 用来判断异常类型是否是数据库的异常
            print("数据库错误")
            return response_failed(ErrorCode.DB, "数据库异常")
        else:
            print("未知错误")
            return response_failed(ErrorCode.UNKNOWN, "未知错误")






