from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.item, name='item'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update_new_item, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete')
]