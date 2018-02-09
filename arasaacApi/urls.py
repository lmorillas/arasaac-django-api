"""arasaacApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from arasaacApi.imagesApi import views
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.documentation import include_docs_urls
from arasaacApi.imagesApi import urls as arasaac_urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#schema_view = get_schema_view(title='Arasaac API')

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Arasaac API')

urlpatterns = [
    #url(r'^api/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title="Arasaac API", 
        description="Arasaac API documentation", 
        public=False)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('arasaacApi.imagesApi.urls')),
    url(r'^schema/$', schema_view, name="swagger schema"),
]
