from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('brand/<int:id>/',views.brand,name='brand'),
    path('car_fulldetails/<int:id>/',views.car_fulldetails,name='car_fulldetails'),
    path('newarival',views.newarival,name='newarival'),
    path('topprice',views.topprice,name='topprice'),
    path('lowprice',views.lowprice,name='lowprice'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('carsell',views.carsell,name='carsell'),
    path('logout/',views.logout,name='logout'),
    path('addcar',views.addcar,name='addcar'),
    path('reqcall',views.callrequest,name='reqcall'),
    path('carsfull',views.carsfull,name='carsfull'),
    path('search/',views.search,name='search'),
    path('filtercolor/<int:id>/',views.filtercolor,name='filtercolor'),
    path('filterbrand/<int:id>/',views.filterbrand,name='filterbrand'),
    path('filterfuel/<int:id>/',views.filterfuel,name='filterfuel'),
    path('filterprice/<int:id>/',views.filterprice,name='filterprice')




]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)