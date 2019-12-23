from django.shortcuts import render
from django.http import HttpResponse

def numbers(request):
    resultado = ''

    for numbers in range(50,151):
        if numbers%5 == 0 and numbers%7 == 0:
            resultado = resultado+"FooBar"+'\n'
        elif numbers%5 == 0:
            resultado = resultado+"Foo"+'\n'
        elif numbers%7 == 0:
            resultado = resultado+"Bar"+'\n'
        else:
            resultado = resultado+str(numbers)+'\n'

    return HttpResponse(resultado)

def queryString(request, queryString):
    array = []

    firstSplit = queryString.split('...')
    for item in firstSplit:
        if '.' in item:
            return HttpResponse('false')
        for letter in item:
            if letter.isdigit():
                array.append(letter)


    while array != []:

        adder = 0
        for i in range(0,2):
            adder = adder + int(array.pop())
        if adder != 10:
            return HttpResponse('false') 

    return HttpResponse('true')    
