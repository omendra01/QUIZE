
from django.urls import path
from quizeapp import views

urlpatterns = [
    path('register/',views.registration,name='register'),
    path('login/',views.login_view,name='login'),
    path('quizetest/',views.quizetest,name='quizetest'),
    path('',views.index,name='index'),
    path('result/',views.result,name='result'),
    path('instruction/',views.instruction,name='instruction')
]
