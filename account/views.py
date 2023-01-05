from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
import logging
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

'''
# posts = list(Post.objects.all().values())
JsonResponse({'posts': posts,
                         'users': users},
'''

@csrf_exempt
def signup(request):
	if request.method == "POST":
		try:
			submitted_values = [request.POST.get('username'),request.POST.get('email'),
			                    request.POST.get('age'),request.POST.get('pwd1'),
			                    request.POST.get('pwd2')] 
			required_values = ['username','email','age','pwd1','pwd2']
			data = zip(required_values,submitted_values)

			# check for user input
			for key, value in zip(required_values,submitted_values):
				if len(value) == 0:
					return JsonResponse({'error': f'invalid {key} value.'})

			# check for password 
			if submitted_values[3] != submitted_values[4]:
				return JsonResponse({'error': "password don't match"})

			# check if age is a valid integer
			try:
				age = int(submitted_values[2])
				if age <= 0:
					return JsonResponse({'error': "invalid sign of age"})
			except ValueError:
				logging.exception("Exception occurred at age conversion")
				return JsonResponse({'error': "invalid value of age exception"})

			user = User.objects.create_user(username=submitted_values[0],
				                       email=submitted_values[1],
				                       age=submitted_values[2],
				                       password=submitted_values[3])
			# if request.FILES['avatar'] == None:
			# 	return JsonResponse({'success': "successfully registerd user"})
			# else:
			# 	# save image
			# 	image = request.FILES['avatar']
			# 	name = image.name
			# 	content_type = image.content_type
			# 	extension = name.split('.')[-1]
			# 	valid_extension = ['jpg','png','jpeg']
			# 	if extension not in valid_extension:
			# 		return JsonResponse({'error': "invalid image type.Extension must be png,jpeg or jpg"})
				# user.avatar = image
			user.save()
				# return JsonResponse({'success': "successfully registerd user"})
			return JsonResponse({'success': "successfully registerd user"})
		except:
			logging.exception("Exception occurred at signup")
			return JsonResponse({'error': "invalid input type occurred"})
	else:
		return JsonResponse({'error': "invalid  request "})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
	return JsonResponse({'error': "invalid  request "})

	





