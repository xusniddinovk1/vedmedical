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

    # ManufacturingOverview
    path('overview/', views.overview_list, name='overview_list'),
    path('overview/create/', views.overview_create, name='overview_create'),
    path('overview/<int:id>/edit/', views.overview_edit, name='overview_edit'),
    path('overview/<int:id>/delete/', views.overview_delete, name='overview_delete'),

    # ManufacturingStat
    path('stat/', views.stat_list, name='stat_list'),
    path('stat/create/', views.stat_create, name='stat_create'),
    path('stat/<int:id>/edit/', views.stat_edit, name='stat_edit'),
    path('stat/<int:id>/delete/', views.stat_delete, name='stat_delete'),

    # ProductionLine
    path('line/', views.line_list, name='line_list'),
    path('line/create/', views.line_create, name='line_create'),
    path('line/<int:id>/edit/', views.line_edit, name='line_edit'),
    path('line/<int:id>/delete/', views.line_delete, name='line_delete'),

    # Partner
    path('partner/', views.partner_list, name='partner_list'),
    path('partner/create/', views.partner_create, name='partner_create'),
    path('partner/<int:id>/edit/', views.partner_edit, name='partner_edit'),
    path('partner/<int:id>/delete/', views.partner_delete, name='partner_delete'),

    # PartnershipBenefit
    path('benefit/', views.benefit_list, name='benefit_list'),
    path('benefit/create/', views.benefit_create, name='benefit_create'),
    path('benefit/<int:id>/edit/', views.benefit_edit, name='benefit_edit'),
    path('benefit/<int:id>/delete/', views.benefit_delete, name='benefit_delete'),

    # GalleryCategory
    path('gallery-category/', views.gallery_category_list, name='gallery_category_list'),
    path('gallery-category/create/', views.gallery_category_create, name='gallery_category_create'),
    path('gallery-category/<int:id>/edit/', views.gallery_category_edit, name='gallery_category_edit'),
    path('gallery-category/<int:id>/delete/', views.gallery_category_delete, name='gallery_category_delete'),

    # Gallery
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:id>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:id>/delete/', views.gallery_delete, name='gallery_delete'),

    # Category
    path('category/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:id>/delete/', views.category_delete, name='category_delete'),

    # News
    path('news/', views.news_list, name='news_list'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/<int:id>/edit/', views.news_edit, name='news_edit'),
    path('news/<int:id>/delete/', views.news_delete, name='news_delete'),
]
