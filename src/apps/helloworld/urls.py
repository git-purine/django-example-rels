from rest_framework import routers

from .views import HelloworldView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"helloworlds", HelloworldView, basename="helloworld")

urlpatterns = router.urls
