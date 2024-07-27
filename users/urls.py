from django.urls import path
from . import views

urlpatterns = [
    path("",views.profiles,name="profiles"),
    path("profile/<str:pk>",views.userProfile,name="user-profile"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('account/',views.userAccount,name="account"),
    path('edit-account/',views.edit_account,name="edit-account"),

]