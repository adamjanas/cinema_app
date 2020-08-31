from app.users.views import CreateAdminView, register
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path("register/", register, name="register"),
    path("create-admin/", CreateAdminView.as_view(), name="create-admin"),
    path(
        "auth/login/",
        views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "auth/logout/",
        views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "auth/password-reset/",
        views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "auth/password-reset/done",
        views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "auth/password-reset/complete",
        views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
