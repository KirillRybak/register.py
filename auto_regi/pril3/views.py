from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime



def index(request):
    return render(request,'pril3/index.html')



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class LoginViev(APIView):
    def post(self, request):
        email = request.data('email')
        password = request.data('password')


        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Пользователь не найден')

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=300),
            'iat': datetime.datetime.utcnow()
        }

        token =jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
            'jwt':token
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        user = User.objects(id=payload['id']).first()
        serializer =  UserSerializer(user)

        if not token:
            raise AuthenticationFailed('Не прошедший проверку подлинности')
        try:
            payload = jwt.decode(token,'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Не прошедший проверку подлинности')
        return Response(serializer.data)


