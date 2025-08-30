from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('sign-up/', views.signup_page, name='signup_page'),
    path('logout/', views.logout_page, name='logout_page'),

    path('my-profile', views.my_profile, name='my_profile', ),
    path('my-profile/edit/', views.profile_edit, name='profile_edit'),

    path('profile/change/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('profile/password/done', PasswordChangeDoneView.as_view(template_name='dashboard/profile/password_done.html'),
         name='password_change_done'),
    # Service
    path("services/", views.service_list, name="service_list"),
    path("services/create/", views.service_create, name="service_create"),
    path("services/<int:pk>/update/", views.service_update, name="service_update"),
    path("services/<int:pk>/delete/", views.service_delete, name="service_delete"),

    # Feature
    path("features/", views.feature_list, name="feature_list"),
    path("features/create/", views.feature_create, name="feature_create"),
    path("features/<int:pk>/update/", views.feature_update, name="feature_update"),
    path("features/<int:pk>/delete/", views.feature_delete, name="feature_delete"),

    # Contact
    path("contacts/", views.contact_list, name="contact_list"),
    path("contacts/create/", views.contact_create, name="contact_create"),
    path("contacts/<int:pk>/update/", views.contact_update, name="contact_update"),
    path("contacts/<int:pk>/delete/", views.contact_delete, name="contact_delete"),

    # Internet
    path("internet/", views.internet_list, name="internet_list"),
    path("internet/create/", views.internet_create, name="internet_create"),
    path("internet/<int:pk>/update/", views.internet_update, name="internet_update"),
    path("internet/<int:pk>/delete/", views.internet_delete, name="internet_delete"),

    # Mission
    path("missions/", views.mission_list, name="mission_list"),
    path("missions/create/", views.mission_create, name="mission_create"),
    path("missions/<int:pk>/update/", views.mission_update, name="mission_update"),
    path("missions/<int:pk>/delete/", views.mission_delete, name="mission_delete"),

    # MissionPoint
    path("missionpoints/", views.missionpoint_list, name="missionpoint_list"),
    path("missionpoints/create/", views.missionpoint_create, name="missionpoint_create"),
    path("missionpoints/<int:pk>/update/", views.missionpoint_update, name="missionpoint_update"),
    path("missionpoints/<int:pk>/delete/", views.missionpoint_delete, name="missionpoint_delete"),

    # Statistic
    path("statistics/", views.statistic_list, name="statistic_list"),
    path("statistics/create/", views.statistic_create, name="statistic_create"),
    path("statistics/<int:pk>/update/", views.statistic_update, name="statistic_update"),
    path("statistics/<int:pk>/delete/", views.statistic_delete, name="statistic_delete"),

    # Value
    path("values/", views.value_list, name="value_list"),
    path("values/create/", views.value_create, name="value_create"),
    path("values/<int:pk>/update/", views.value_update, name="value_update"),
    path("values/<int:pk>/delete/", views.value_delete, name="value_delete"),

    # Achievement
    path("achievements/", views.achievement_list, name="achievement_list"),
    path("achievements/create/", views.achievement_create, name="achievement_create"),
    path("achievements/<int:pk>/update/", views.achievement_update, name="achievement_update"),
    path("achievements/<int:pk>/delete/", views.achievement_delete, name="achievement_delete"),

    # Member
    path("members/", views.member_list, name="member_list"),
    path("members/create/", views.member_create, name="member_create"),
    path("members/<int:pk>/update/", views.member_update, name="member_update"),
    path("members/<int:pk>/delete/", views.member_delete, name="member_delete"),

    # History
    path("history/", views.history_list, name="history_list"),
    path("history/create/", views.history_create, name="history_create"),
    path("history/<int:pk>/update/", views.history_update, name="history_update"),
    path("history/<int:pk>/delete/", views.history_delete, name="history_delete"),
]
