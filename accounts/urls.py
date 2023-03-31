from django.urls import path
from accounts.views import BlogPostListView, CustomTokenObtainPairView, Registrationview, VerifyView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', Registrationview.as_view(), name='register'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/blog-posts/', BlogPostListView.as_view()),
    path('api/token-verify/', TokenVerifyView.as_view()),

]
