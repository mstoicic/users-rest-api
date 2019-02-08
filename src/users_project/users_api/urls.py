from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

#Created basic router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)    # No need for base_name becouse its model user
router.register('login', views.LoginViewSet, base_name = 'login')
router.register('feed', views.UserProfileFeedViewSet)   # No need for base_name becouse its model user


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
