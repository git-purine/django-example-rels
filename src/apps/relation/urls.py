from rest_framework import routers

from .views import RelationView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"oneselfs", RelationView, basename="helloworld")

urlpatterns = router.urls
