import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account


class SignUpView(View):
	def post(self,request):
		data = json.loads(request.body)
		try:
			if Account.objects.filter(email = data['email']).exists():
				return HttpResponse(status=400)

			Account.objects.create(
				email = data['email'],
				password = data['password']
				)
			return JsonResponse({'message': '회원가입 성공'},status=200)
		except KeyError:
			return JsonResponse({"message":"INVALID_KEYS"},status=400)



class SignInView(View):
	def post(self,request):
		data = json.loads(request.body)

		try:
			if Account.objects.filter(email=data['email']).exists():
				user = Account.objects.get(email=data['email'])
			
				if user.password ==data['password']:
					return JsonResponse({'message':f'{user.email}님 로그인 되셨습니다.'},status=200)
				
				return JsonResponse({'message':'비밀번호가 틀렸어요.'},status=401)
		
		except KeyError:
			return JsonResponse({'message':'미등록 이메일 입니다.'},status=400)
