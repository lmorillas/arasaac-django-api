
from django.conf.urls import url, include
from arasaacApi.imagesApi import views
from rest_framework_mongoengine import routers as merouters

merouter = merouters.DefaultRouter()
merouter.register(r'en/images', views.ImageENViewSet)
merouter.register(r'es/images', views.ImageESViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls