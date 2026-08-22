from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from complaints import views
from users import views as user_views


urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'report/',
        views.report_complaint,
        name='report_complaint'
    ),

    path(
        'report/success/',
        views.report_success,
        name='report_success'
    ),

    path(
        'register/',
        user_views.register,
        name='register'
    ),

    path(
        'login/',
        user_views.user_login,
        name='login'
    ),

    path(
        'logout/',
        user_views.user_logout,
        name='logout'
    ),

    path(
        'my-reports/',
        views.my_reports,
        name='my_reports'
    ),

    path(
        'dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'dashboard/update-status/<int:complaint_id>/',
        views.update_complaint_status,
        name='update_complaint_status'
    ),

    path(
        'dashboard/assign-department/<int:complaint_id>/',
        views.assign_department,
        name='assign_department'
    ),
]


# Serve uploaded images during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )