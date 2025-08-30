from django import forms
from medical.models import (
    Service, Feature, Contact, Internet,
    Mission, MissionPoint, Statistic, Value,
    Achievement, Member, History
)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class InternetForm(forms.ModelForm):
    class Meta:
        model = Internet
        fields = "__all__"


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = "__all__"


class MissionPointForm(forms.ModelForm):
    class Meta:
        model = MissionPoint
        fields = "__all__"


class StatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields = "__all__"


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = "__all__"


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = "__all__"


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = "__all__"
