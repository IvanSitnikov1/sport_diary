from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

from api.views import ProgramCreateView, WorkoutCreate


urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('programs/', ProgramCreateView.as_view(), name='program-create'),
    path('workout/', WorkoutCreate.as_view(), name='workout-create'),
]
