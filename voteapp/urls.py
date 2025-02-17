from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from listings.views import CandidatListAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="The summer show",
      default_version='v1',
      description="TheSummer show documentation",
      terms_of_service="",
      contact=openapi.Contact(email="thesummershow@site.com"),
      license=openapi.License(name=""),

   ),
   public=False,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('listings.urls')),
    path('documentation<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)