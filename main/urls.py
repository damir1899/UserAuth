from django.urls import path
from .views import IndexView, AddProductView, ProductView, \
    CategoryView, LogoutUserView, SignUpUserView, \
        SignInUserView, UserProfileView, UserEditProfileView, \
            SettingsView

urlpatterns = [
    path("", IndexView),
    path("add/", AddProductView),
    path("product/", ProductView),
    path("category/", CategoryView),
    path('signup/', SignUpUserView),
    path('signin/', SignInUserView),
    path('logout/', LogoutUserView),
    path('profile/', UserProfileView),
    path('profile/edit/', UserEditProfileView),
    path('settings/', SettingsView),
    ]