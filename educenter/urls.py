"""educenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from educenterapp.api_views import SubjectViewSet, ResultViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet)
router.register(r'result', ResultViewSet)
router.register(r'person', PersonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('educenterapp.urls', namespace='educenter')),
    path('test/', include('testapp.urls', namespace='test')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls)),]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]

