
from django.conf.urls import url, include
from rest_framework import routers
from arasaacApi.imagesApi import views
from rest_framework_mongoengine import routers as merouters

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


merouter = merouters.DefaultRouter()
#merouter.register('/{lang}/images', views.ImageESViewSet, base_name='images_es')
merouter.register('(?P<lang>[a-z]+)/images', views.ImageESViewSet, base_name='images_es')
#merouter.register(r'/images', views.ImageESViewSet, base_name='images_en')

urlpatterns = [

]
 
urlpatterns += merouter.urls
urlpatterns += router.urls