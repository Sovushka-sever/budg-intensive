import time

from django.contrib.auth import login, logout
from django.utils.deprecation import MiddlewareMixin


class FakeUser:
    # определите у пользователя аттрибуты auth

    # def __init__(self, user):
    #     self.auth = user.auth
    pass


# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):

    # def process_request(self, request):
    #     self.begin_timestamp = time.time()
    #     print(f"Время до выполнения запроса: {self.begin_timestamp}")
    #     time.sleep(1)
    #     user = FakeUser()
    #     if request.auth == 'VALID_TOKEN':
    #         user.auth = True
    #         request.auth = True
    #     else:
    #         user.auth = False
    #         request.auth = False
    #
    #
    #     return self.get_response(request)
    #
    # def process_response(self, request, response):
    #     end_timestamp = time.time()
    #     runtime = end_timestamp - self.begin_timestamp
    #     request.runtime = runtime
    #     print(f"Время после выполнения запроса: {end_timestamp}")
    #     print(f"Время выполнения запроса: {request.runtime}")
    #     return response

    # def __call__(self, request):
    #
    #     response = None
    #     if hasattr(self, 'process_request'):
    #
    #         response = self.process_request(request)
    #     response = response or self.get_response(request)
    #     if hasattr(self, 'process_response'):
    #
    #         response = self.process_response(request, response)
    #     return response

        # request.runtime = None
        #
        # begin_timestamp = time.time()
        # print(f"Время до выполнения запроса: {begin_timestamp}")
        # time.sleep(1)
        #
        # response = self.get_response(request)
        #
        # end_timestamp = time.time()
        # request.runtime = end_timestamp - begin_timestamp
        # print(f"Время после выполнения запроса: {end_timestamp}")
        # print(f"Время выполнения запроса: {request.runtime}")


        # user = FakeUser()
        # if request.auth == 'VALID_TOKEN':
        #     user.auth = True
        #     request.auth = True
        # else:
        #     user.auth = False
        #     request.auth = False
        #
        # return response

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
            print(f"Время до выполнения запроса: {self.begin_timestamp}")
        time.sleep(1)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
            print(f"Время после выполнения запроса: {self.end_timestamp}")
            print(f"Время выполнения запроса: {request.runtime}")
        return response

    def process_request(self, request):
        self.begin_timestamp = time.time()
        return self.get_response(request)

    def process_response(self, request, response):
        self.end_timestamp = time.time()
        request.runtime = self.end_timestamp - self.begin_timestamp
        user = FakeUser()
        if request.auth == 'VALID_TOKEN':
            user.auth = True
            request.auth = True
        else:
            user.auth = False
            request.auth = False
        return response


"""
SessionMiddleware - включает поддержку механизма сессий в Django-проекте. 
То есть по Session ID, который передаётся в Cookies, находит данные сессии в бекенде для хранения сессий.
(управляет состоянием сеанса для пользователя)

CsrfViewMiddleware - проверяет запросы с данными от клиента на наличие CSRF-токена, дабы предотвратить подделку запроса
(гарантирует, что токен CSRF присутствует и действителен при отправке формы)

AuthenticationMiddleware - находит по сессии Django-пользователя, подставляя его в поле user объекта request 
(добавить user атрибут к HttpRequest объекту)
"""





