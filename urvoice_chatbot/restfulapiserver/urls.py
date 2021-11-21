from django.conf.urls import url, include
from psycologyconsult import views
from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import TemplateView
#from rest_framework_swagger.views import get_swagger_view



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    path('chat/', views.chat_service),
    #re_path('', TemplateView.as_view(template_name='addresses/chat_test.html')),
]