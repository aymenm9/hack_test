from django.urls import path
from . import views
urlpatterns=[
    path('users/',views.UserView.as_view(),name='create user'),
    path('products/',views.ProductVeiw.as_view(),name='Product create list'),
    path('products/<int:id>/',views.ProductVeiwDetails.as_view(),name='Product  detials'),
]