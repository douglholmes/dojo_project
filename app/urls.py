from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('main', views.main),
    path('order', views.order),
    path('process_order', views.process_order),
    path('view_order/<int:order_id>', views.view_order),
    path('delete_order/<int:order_id>', views.delete_order),

]
