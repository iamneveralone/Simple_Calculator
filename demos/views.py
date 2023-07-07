from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request): # 첫번째 인자로 무조건 request 들어와야 함
    # return HttpResponse('계산기 기능 구현 시작입니다.')
    
    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    # (html에서 num1, num2, operators 값들을 보내줘야 함)
    # html로부터 num1, num2가 text로 넘어왔기 때문에 int로 형변환 해준 것
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0
    
    # 3. 응답

    return render(request, 'calculator.html', {'result' : result})
    # html에서 데이터 출력해주기 위해서는 view에서 데이터를 넘겨줘야 함
    # 즉, result를 넘겨줘야 함 
    # => view의 result 값을 calculator.html에서 'result'라는 변수로 사용 가능



# view는 urls.py를 타고 받아야 함 (즉, urls.py가 view를 불러줘야 함)
# => 그래서 이 함수를 실행시키려면 urls.py에 코드를 작성해줘야 함

# HttpRequest 클래스 : 클라이언트로부터 들어오는 요청의 정보를 담을 수 있음
# => request : HttpRequest 객체
# HttpResponse 클래스 : 클라이언트에게 응답해주는 정보를 담을 수 있음

# 장고는 request 객체와 response 객체로 상태를 서버와 클라이언트가 주고 받음
# 1. 특정 페이지가 Request되면, 장고는 메타데이터를 포함하는 HttpRequest 객체를 생성
# 2. 장고는 urls.py에서 import한 특정 view 클래스/함수에 첫 번째 인자로 해당 HttpRequest 객체 request를 전달
# 3. 해당 view는 결과값을 HttpResponse (또는 JsonResponse) 객체에 담아 전달
# 이를 위해서 장고는 django.http 모듈에서 HttpRequest와 HttpResponse API 제공

# 그냥 return HttpResponse("계산기 기능 구현") 해도 웹 페이지에 문구 띄울 수 있음
# 그러나, templates 폴더에 생성한 caculator.html의 내용을 웹 페이지 화면에 띄우고 싶다면?
# => render 함수 사용
# => 인자로 받은 HttpResquest 객체인 request를 templates 폴더의 context(html 파일)과 엮어
#    HttpResponse 객체로 반환해주는 함수

# request : HttpRequest 객체
# request.GET : (Django 문법) request에 전달받은 내용들을 사전형 데이터로 가져옴
# request.GET.get() : (Django 문법) 사전형 데이터의 key를 입력하면 value를 가져옴

# view를 먼저 작성하고, 필요에 따라서 template을 이후에 구현