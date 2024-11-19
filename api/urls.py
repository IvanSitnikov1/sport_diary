from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

from api.views import ProgramCreateView, WorkoutCreate, \
    ProgramRetrieveUpdateDestroyView, WorkoutDestroy, UserModelViewSet


router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('programs/', ProgramCreateView.as_view(), name='program-list-create'),
    path(
        'programs/<int:pk>/',
        ProgramRetrieveUpdateDestroyView.as_view(),
        name='program-retrieve-update-destroy',
    ),
    path('workouts/', WorkoutCreate.as_view(), name='workout-create'),
    path('workouts/<int:pk>/', WorkoutDestroy.as_view(), name='workout-destroy'),
]
