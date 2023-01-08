from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('menu-items', views.MenuItemsView.as_view()),
    path('secret/', views.secret),
    path('token/', obtain_auth_token),
    path('manager/', views.manager_view),
    path('throttle_check/', views.throttle_check)
]
