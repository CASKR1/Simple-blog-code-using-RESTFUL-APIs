from django.contrib import admin
from django.urls import path, include
from blog import views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', views.PostViewSet, basename='post-view-set')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
]
