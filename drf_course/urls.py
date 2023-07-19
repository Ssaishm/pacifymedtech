from django.urls import path
from django.contrib import admin
from awards import views as awards_views
from core import views as core_views
from demo import views as demo_views
from distribution import views as distribution_views
from careers import views as careers_views
from home import views as home_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
#######


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    #path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
    path('democontact/', demo_views.DemoContactAPIView.as_view()),
    path('wcontact/', core_views.wContactAPIView.as_view()),
    path('discontacts/', distribution_views.disContactAPIView.as_view()),
    path('careers/', careers_views.careers_list),
    path('careers/<int:id>', careers_views.careers_detail),
    path('home/',home_views.home_list),
    path('home/<int:id>',home_views.home_detail),
    path('hblogs/',home_views.hblogs_list),
    path('hblogs/<int:id>',home_views.hblogs_detail),
    path('hImage/',home_views.hImage_list),
    path('hImage/<int:id>',home_views.hImage_detail),
    path('hLogo/',home_views.hLogo_list),
    path('hLogo/<int:id>',home_views.hLogo_detail),
    path('aImage/',awards_views .AImage_list),
    path('aImage/<int:id>',awards_views .AImage_detail),
    path('awards/',awards_views.awards_list),
    path('awards/<int:id>',awards_views.awards_detail),
    path('exceldemo/',demo_views.ExcelPageView.as_view(), name='excel_demo.html'),
    path('export/excel', demo_views.export_users_xls, name='export_exceldemo'),
    path('excelcore/',core_views.ExcelPageView.as_view(), name='excel_core.html'),
    path('export/excelcore', core_views.export_users_xls, name='export_excelcore'),
    path('exceldistribution/',distribution_views.ExcelPageView.as_view(), name='excel_distribution.html'),
    path('export/exceldistribution', distribution_views.export_users_xls, name='export_exceldistribution'),




]

#urlpatterns = format_suffix_patterns(urlpatterns)
######################
#
# remove detailed error
# put standard error page after completion of website
# remove detail pages
urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)