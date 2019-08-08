from django.conf.urls import url, include
from user import views

app_name = 'user'
urlpatterns = [
    url('^sign_up/$', views.sign_up),
    url('^login/$', views.login),
    url('^sync_score/$', views.sync_score),
    url('^get_questions/$', views.get_questions),

]
