from django.urls import path
from . import views
from wiselane import views


#urls
urlpatterns = [
		path('', views.index, name="home"),
		]

