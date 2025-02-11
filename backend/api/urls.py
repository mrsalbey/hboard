from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CohortViewSet, SprintsViewSet

router = DefaultRouter()

# router.register('users', FoodgramUserViewSet, basename='users')
router.register('cohorts', CohortViewSet, basename='cohorts')
router.register('sprints', SprintsViewSet, basename='sprints')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('v1/', include(router.urls)),
]
