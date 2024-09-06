from django.urls import path
from posapp import views
urlpatterns = [
    path('items/', views.items_list),
    path('items/<int:pk>/', views.items_detail),
    path('items/makanan/', views.items_makanan_list),
    path('items/minuman/', views.items_minuman_list),
    path('create-pesanan/', views.create_pesanan),
]