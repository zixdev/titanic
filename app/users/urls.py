from django.urls import path

from app.users.views import CreateUserView, CreateTokenView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
