from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from medical.models import (
    Service, Feature, Contact, Internet,
    Mission, MissionPoint, Statistic, Value,
    Achievement, Member, History
)
from .forms import (
    ServiceForm, FeatureForm, ContactForm, InternetForm,
    MissionForm, MissionPointForm, StatisticForm, ValueForm,
    AchievementForm, MemberForm, HistoryForm, ProfileForm
)


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


def login_page(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")
        remember = request.POST.get("remember_me")  # checkbox nomi

        user = authenticate(request, phone_number=phone, password=password)
        if user:
            login(request, user)

            if not remember:
                # Sessiyani brauzer yopilganda tugatish
                request.session.set_expiry(0)

            return redirect("home_page")
        else:
            return render(request, "dashboard/login.html", {"error": "Incorrect credentials"})

    return render(request, "dashboard/login.html")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


@login_required_decorator
def my_profile(request):
    ctx = {
        'user': request.user,
    }
    return render(request, 'dashboard/profile/profile.html', ctx)


@login_required_decorator
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('my_profile')  # profil sahifasiga qaytish
    else:
        form = ProfileForm(instance=user)

    ctx = {
        'form': form
    }

    return render(request, 'dashboard/profile/profile_edit.html', ctx)


@method_decorator(login_required, name='dispatch')
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'dashboard/profile/password_change.html'
    success_url = reverse_lazy('password_change_done')


# @login_required_decorator
# def home_page(request):
    # users = User.objects.all()
    # news = News.objects.all()
    # courses = Course.objects.all()
    # lessons = Lesson.objects.all()

    # items = [
    #     {
    #         "icon": "fa-users",
    #         "color": "#3b82f6",  # blue-500
    #         "count": users.count(),
    #         "label": "Users",
    #         "chart_data": [users.count(), users.count() // 2, users.count() // 3]
    #     },
    #     {
    #         "icon": "fa-book",
    #         "color": "#10b981",  # green-500
    #         "count": news.count(),
    #         "label": "News",
    #         "chart_data": [news.count(), news.count() // 2, news.count() // 3]
    #     },
    #     {
    #         "icon": "fa-bell",
    #         "color": "#ef4444",  # red-500
    #         "count": courses.count(),
    #         "label": "Courses",
    #         "chart_data": [courses.count(), courses.count() // 2, courses.count() // 3]
    #     },
    #     {
    #         "icon": "fa-star",
    #         "color": "#facc15",  # yellow-500
    #         "count": lessons.count(),
    #         "label": "Lessons",
    #         "chart_data": [lessons.count(), lessons.count() // 2, lessons.count() // 3]
    #     },
    # ]
    # return render(request, 'dashboard/index.html', {'items': items})


# Generic function for CRUD
def list_view(request, model, template, context_name):
    objects = model.objects.all()
    return render(request, template, {context_name: objects})


def create_view(request, form_class, template, redirect_url):
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, template, {"form": form})


def update_view(request, model, form_class, pk, template, redirect_url):
    obj = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=obj)
    return render(request, template, {"form": form})


def delete_view(request, model, pk, template, redirect_url, context_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect(redirect_url)
    return render(request, template, {context_name: obj})


# ---------------- SERVICE ----------------
def service_list(request):
    return list_view(request, Service, "dashboard/services/list.html", "services")


def service_create(request):
    return create_view(request, ServiceForm, "dashboard/services/form.html", "service_list")


def service_update(request, pk):
    return update_view(request, Service, ServiceForm, pk, "dashboard/services/form.html", "service_list")


def service_delete(request, pk):
    return delete_view(request, Service, pk, "dashboard/services/confirm_delete.html", "service_list", "service")


# ---------------- FEATURE ----------------
def feature_list(request):
    return list_view(request, Feature, "dashboard/features/list.html", "features")


def feature_create(request):
    return create_view(request, FeatureForm, "dashboard/features/form.html", "feature_list")


def feature_update(request, pk):
    return update_view(request, Feature, FeatureForm, pk, "dashboard/features/form.html", "feature_list")


def feature_delete(request, pk):
    return delete_view(request, Feature, pk, "dashboard/features/confirm_delete.html", "feature_list", "feature")


# ---------------- CONTACT ----------------
def contact_list(request):
    return list_view(request, Contact, "dashboard/contacts/list.html", "contacts")


def contact_create(request):
    return create_view(request, ContactForm, "dashboard/contacts/form.html", "contact_list")


def contact_update(request, pk):
    return update_view(request, Contact, ContactForm, pk, "dashboard/contacts/form.html", "contact_list")


def contact_delete(request, pk):
    return delete_view(request, Contact, pk, "dashboard/contacts/confirm_delete.html", "contact_list", "contact")


# ---------------- INTERNET ----------------
def internet_list(request):
    return list_view(request, Internet, "dashboard/internet/list.html", "internets")


def internet_create(request):
    return create_view(request, InternetForm, "dashboard/internet/form.html", "internet_list")


def internet_update(request, pk):
    return update_view(request, Internet, InternetForm, pk, "dashboard/internet/form.html", "internet_list")


def internet_delete(request, pk):
    return delete_view(request, Internet, pk, "dashboard/internet/confirm_delete.html", "internet_list", "internet")


# ---------------- MISSION ----------------
def mission_list(request):
    return list_view(request, Mission, "dashboard/missions/list.html", "missions")


def mission_create(request):
    return create_view(request, MissionForm, "dashboard/missions/form.html", "mission_list")


def mission_update(request, pk):
    return update_view(request, Mission, MissionForm, pk, "dashboard/missions/form.html", "mission_list")


def mission_delete(request, pk):
    return delete_view(request, Mission, pk, "dashboard/missions/confirm_delete.html", "mission_list", "mission")


# ---------------- MISSION POINT ----------------
def missionpoint_list(request):
    return list_view(request, MissionPoint, "dashboard/missionpoints/list.html", "missionpoints")


def missionpoint_create(request):
    return create_view(request, MissionPointForm, "dashboard/missionpoints/form.html", "missionpoint_list")


def missionpoint_update(request, pk):
    return update_view(request, MissionPoint, MissionPointForm, pk, "dashboard/missionpoints/form.html",
                       "missionpoint_list")


def missionpoint_delete(request, pk):
    return delete_view(request, MissionPoint, pk, "dashboard/missionpoints/confirm_delete.html", "missionpoint_list",
                       "missionpoint")


# ---------------- STATISTIC ----------------
def statistic_list(request):
    return list_view(request, Statistic, "dashboard/statistics/list.html", "statistics")


def statistic_create(request):
    return create_view(request, StatisticForm, "dashboard/statistics/form.html", "statistic_list")


def statistic_update(request, pk):
    return update_view(request, Statistic, StatisticForm, pk, "dashboard/statistics/form.html", "statistic_list")


def statistic_delete(request, pk):
    return delete_view(request, Statistic, pk, "dashboard/statistics/confirm_delete.html", "statistic_list",
                       "statistic")


# ---------------- VALUE ----------------
def value_list(request):
    return list_view(request, Value, "dashboard/values/list.html", "values")


def value_create(request):
    return create_view(request, ValueForm, "dashboard/values/form.html", "value_list")


def value_update(request, pk):
    return update_view(request, Value, ValueForm, pk, "dashboard/values/form.html", "value_list")


def value_delete(request, pk):
    return delete_view(request, Value, pk, "dashboard/values/confirm_delete.html", "value_list", "value")


# ---------------- ACHIEVEMENT ----------------
def achievement_list(request):
    return list_view(request, Achievement, "dashboard/achievements/list.html", "achievements")


def achievement_create(request):
    return create_view(request, AchievementForm, "dashboard/achievements/form.html", "achievement_list")


def achievement_update(request, pk):
    return update_view(request, Achievement, AchievementForm, pk, "dashboard/achievements/form.html",
                       "achievement_list")


def achievement_delete(request, pk):
    return delete_view(request, Achievement, pk, "dashboard/achievements/confirm_delete.html", "achievement_list",
                       "achievement")


# ---------------- MEMBER ----------------
def member_list(request):
    return list_view(request, Member, "dashboard/members/list.html", "members")


def member_create(request):
    return create_view(request, MemberForm, "dashboard/members/form.html", "member_list")


def member_update(request, pk):
    return update_view(request, Member, MemberForm, pk, "dashboard/members/form.html", "member_list")


def member_delete(request, pk):
    return delete_view(request, Member, pk, "dashboard/members/confirm_delete.html", "member_list", "member")


# ---------------- HISTORY ----------------
def history_list(request):
    return list_view(request, History, "dashboard/history/list.html", "histories")


def history_create(request):
    return create_view(request, HistoryForm, "dashboard/history/form.html", "history_list")


def history_update(request, pk):
    return update_view(request, History, HistoryForm, pk, "dashboard/history/form.html", "history_list")


def history_delete(request, pk):
    return delete_view(request, History, pk, "dashboard/history/confirm_delete.html", "history_list", "history")
