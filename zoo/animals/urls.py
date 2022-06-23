from django.urls import path
from .views import AnimalListView, status_view, ContactFormView, AnimalDetailView, AnimalCreateView, AnimalUpdateView, \
    AnimalDeleteView, UserCreateView, LoginUserView, LogoutUserView

app_name = 'animals'

urlpatterns = [
    path('', AnimalListView.as_view(), name='index'),
    path('status/', status_view, name='status'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name='detail'),
    path('create/', AnimalCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AnimalUpdateView.as_view(), name='update'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('delete/<int:pk>/', AnimalDeleteView.as_view(), name='delete'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout')
]
