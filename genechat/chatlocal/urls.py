
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^messages/', views.MessageView.as_view({'get': 'list', 'post': 'create'}), name='messages'),
    url(r'^users/(?P<pk>[^/]+)$', views.UserView.as_view({'get': 'retrieve'}), name='message'),
    url(r'^users/', views.UserView.as_view({'get': 'list'}), name='users'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        ]
