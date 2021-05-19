from django.urls import path
from AuthAppApi.Views import UsersView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('signup/', UsersView.UserSignupView().as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('update/<int:pk>/', UsersView.UserUpdateView().as_view(), name='update'),
    path('delete/<int:pk>/', UsersView.UserDeleteView().as_view(), name='delete'),
    path('logout/', UsersView.LogoutView.as_view(), name = 'logout')
    
]
