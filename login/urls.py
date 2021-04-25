from django.urls import path
from . import views

# urlpatterns = [
# 	path('',views.login_form, name='login'),
# 	path('submit_form', views.submit_form, name='submit_form')
# 	]

urlpatterns = [
	path("register", views.register, name="register"),
	path('login',views.login, name='login'),
	path('logout',views.logout, name='logout')

	]