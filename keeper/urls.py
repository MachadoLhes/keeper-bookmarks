from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from bookmark import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookmarks', views.BookmarkViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]