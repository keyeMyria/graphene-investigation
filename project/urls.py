"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from inspect import isclass

from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt

import debug_toolbar
from dynamic_rest.routers import DynamicRouter
from graphene_django.views import GraphQLView

from drest import views

# auto-register views
router = DynamicRouter()

for name in dir(views):
    view = getattr(views, name)
    if isclass(view) and getattr(view, 'serializer_class', None):
        router.register_resource(view, namespace='api')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.DEBUG:
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
