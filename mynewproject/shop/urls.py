from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.ProductList, name='list'),
    path('create_product/',views.create_product, name='create_product'),
    path('register/',views.registerview,name='register'),
    path('<id>/detail',views.detail_view,name='details'), 
]
