from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
                    HomeView,
                    CreateConfigurationView,
                    UpdateConfigurationView,
                    ConfigureView, 
                    about_us,
                    delete_configuration_ajax, 
                    send_offer_ajax
                )


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('configure/create/<int:car_id>/', CreateConfigurationView.as_view(), name='create_config'),
    path('configure/update/<int:config_id>/', UpdateConfigurationView.as_view(), name='update_config'),
    path('configure/', ConfigureView.as_view(), name='configure_car_list'),
    path('about_us/', about_us, name='about-us'),
    path('delete-configuration/', delete_configuration_ajax, name='delete_configuration_ajax'),
    path('send-offer/', send_offer_ajax, name='send_offer_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


