from .models import UserInfo
from MAINAPP.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class HandleLogin(APIView):
    def post(self,request):
        clientData = {}
        serverData = UserInfo.objects.all()
        serializer = UserSerializer(data = request.data)
        if(serializer.is_valid(raise_exception=True)):
            # data =>{'username' : 'usernameValue' , 'password' : 'passwordValue'}
            data = dict(serializer.data)
            if('username' in data.keys()):
                None