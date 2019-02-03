from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    path('', include('authentication.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
