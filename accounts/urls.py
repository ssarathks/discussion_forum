from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name='accounts'

urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='homepage'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/',LogoutView.as_view(),name='logout'),
    url(r'^landing/',views.LandingPageView.as_view(),name='landing'),
    url(r'^createitem/',views.itemCreateView,name='item_create'),
    url(r'^listitem/',views.ItemListView.as_view(),name='itemlist'),
    url(r'^item/(?P<pk>\d+)/',views.ItemDetailView.as_view(),name='item_detail')


]
