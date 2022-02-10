
from django.urls import path
from lineas import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('lineas', views.LineaView),
router.register('estaciones', views.EstacionView)
router.register('usuario', views.UsuarioView )
router.register('viajes', views.ViajesView)



urlpatterns = router.urls 

# urlpatterns = [
#     path('lineas', LineaView.as_view(), name="linea") 
# ]
