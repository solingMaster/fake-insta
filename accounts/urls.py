from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [
    #signup으로 들어오면 회원가입 폼 볼수있게 , 회원가입 시켜주기 작업이 필요함.
    path('signup/', views.signup, name='signup'),
    #로그인 경로 만들어주기
    path('login/', views.login, name='login'),
    #로그아웃
    path('logout/', views.logout, name='logout')
    ]