from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class Root(APIView):
    def get(self,reqeust):
        return Response({'msg':'hello,world!'},status=status.HTTP_200_OK)