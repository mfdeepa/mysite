from django.http import HttpResponse



def say_hello(request):
    return HttpResponse('Hello Everyone, My first Django project!')

def say_hello_with_name(request, name):
    print(request.headers)
    #print(request.content_type)
    return HttpResponse('Hello Everyone! My name is %s and this is my first Django project : mysite' % name)