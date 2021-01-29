from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views

app_name ='core'
urlpatterns = [
    path('',views.home_view, name='home'),
    path('product_detail/<int:pk>', views.product_detail, name="product_detail")

]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)