from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/organization/', include('organization.urls')),
] + debug_toolbar_urls()
