from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from message_app.models import Message,Quota
from message_app.serializers import MessageSerializer
from django.contrib.auth.models import User
from datetime import date
from rest_framework.authtoken.models import Token

class MessageAPI(APIView):
    def get(self,request):
        try:
            user_id = request.GET.get('id')
            user = User.objects.get(id=user_id)
        except:return Response(status=500)
        try:
            q = Quota.objects.get(user=user)
            if q.date == date.today():
                if q.view == 6:
                    return Response({"status":"Quota Exceeded"},status=200)
                q.view += 1
                q.save()
            else:
                q.date = date.today()
                q.view = 1
                q.save()

        except Quota.DoesNotExist : 
            q = Quota()
            q.date = date.today()
            q.view = 1
            q.user = user
            q.save()
            


        content = Message.objects.all()
        content = MessageSerializer(content,many=True).data
        return Response(content,status=200)

def token_generate(request):
    if request.method == 'GET':
        print(User.objects.values())
        user_id = request.GET.get('id')
        print(user_id)
        user = User.objects.get(id=user_id)
        print(user)
        try:
            q = Quota.objects.get(user=user)
        except Quota.DoesNotExist : 
            q = Quota()
            q.date = date.today()
            q.view = 1
            q.user = user
        q.save()
        return redirect(f'api/messages?id={user_id}')
