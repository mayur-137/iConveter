from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import apis
from apis import urls
from . import views
from Backend import settings

urlpatterns = [
    path('admin', admin.site.urls),
    # path('', views.index, name='name'),
    path('', include(apis.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
