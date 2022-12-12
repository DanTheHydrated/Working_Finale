from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'users', views.Get_Profile)
router.register(r'posts', views.Get_Posts)
router.register(r'followers', views.Follow)


urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserListView.as_view()),
    path('user/signup/', views.UserCreate.as_view(), name="create_user"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


