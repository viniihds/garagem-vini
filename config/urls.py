from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from garagem.views import MarcaViewSet, CorViewSet, CategoriaViewSet, AcessorioViewSet, VeiculoViewSet, ModeloViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"veiculos", VeiculoViewSet)
router.register(r"modelos", ModeloViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root = settings.MEDIA_ROOT)
