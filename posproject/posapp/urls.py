from django.urls import path
from posapp import views
urlpatterns = [
    path('items/', views.items_list),
    path('items/<int:pk>/', views.items_detail),
]