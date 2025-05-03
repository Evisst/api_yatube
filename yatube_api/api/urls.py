from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

posts_router = nested_routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    # Получение токена по логину/паролю
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # Основные ресурсы
    path('', include(router.urls)),
    # Вложенные комментарии
    path('', include(posts_router.urls)),
]
