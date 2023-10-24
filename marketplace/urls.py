from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='Marketplace API',
        default_version='v1',
        contact=openapi.Contact(url='https://t.me/dimanitto'),
    ),
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/docs/')),
    path('backend/', include('core.urls', namespace='core')),
    path(
        'backend/docs/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path('backend/admin/', admin.site.urls),
]
