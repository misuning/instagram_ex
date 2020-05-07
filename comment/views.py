import json
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Comment

# Create your views here.

class CommentView(View):
	def post(self,request):
		data = json.loads(request.body)
		try:
			Comment.objects.create(
					name = data['name'],
					text = data['text']
					)
			return HttpResponse(status =200)
			
		except KeyError:
			return JsonResponse({'message':'INVALID_KEYS'},status=400)
		

	
	def get(self,request):
		comment_data = list(Comment.objects.values())

		return JsonResponse({'data':comment_data},status =200)


