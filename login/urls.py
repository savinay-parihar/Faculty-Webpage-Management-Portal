from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='login'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^login/$',auth_views.login,{'template_name': 'registration/user_login.html'},name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^portal/$',views.portal,name='portal'),
    url(r'^portal/home/$',views.profile_home_page,name='portal_home'),
    url(r'^portal_form/home/$', views.profile_home, name='portal_form_home'),
    url(r'^portal_form/teaching/$',views.Teaching,name='portal_form_teaching'),
    url(r'^portal/teaching/$', views.Teaching_page, name='portal_teaching'),
    url(r'^portal_form/project/$', views.Project, name='portal_form_project'),
    url(r'^portal/project/$', views.Project_page, name='portal_project'),
    url(r'^portal_form/publication/$', views.Publication, name='portal_form_publication'),
    url(r'^portal/publication/$', views.Publication_page, name='portal_publication'),
    url(r'^portal_form/experience/$', views.Experience, name='portal_form_experience'),
    url(r'^portal/experience/$', views.Experience_page, name='portal_experience'),
    url(r'^portal_form/qualification/$', views.Qualification, name='portal_form_qualification'),
    url(r'^portal/qualification/$', views.Qualification_page, name='portal_qualification'),
    url(r'^fac_home/(?P<username>\w+)/$',views.fac_home, name="fac_home"),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.password_reset_complete,name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
