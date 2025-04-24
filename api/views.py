from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .serializer import UserSerializer, CreateUserSerializerOutPut, ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={201: CreateUserSerializerOutPut},
    )
    def post(self,request):
        user_Serialized = UserSerializer(data = request.data)
        print(user_Serialized)
        if user_Serialized.is_valid():
            print('is hire ')
            user = user_Serialized.save()
            refresh = RefreshToken.for_user(user)
            out_data = CreateUserSerializerOutPut({
                'user':UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

            return Response(out_data.data,status=status.HTTP_200_OK )

        
        return Response(user_Serialized.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductVeiw(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

class ProductVeiwDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

