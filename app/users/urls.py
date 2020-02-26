from django.urls import path

from app.users.views import CreateUserView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
]
