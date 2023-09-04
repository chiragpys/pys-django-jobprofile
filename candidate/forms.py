from django import forms
from .models import CandidateProfile, SkillDetail, ExperienceDetail, StudyDetail


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'created': forms.DateInput(attrs={'type': 'date'})
        }


class StudyForm(forms.ModelForm):
    class Meta:
        model = StudyDetail
        exclude = ['candidate']
        widgets = {
            'passing_year': forms.DateInput(attrs={'type': 'date'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        exclude = ['candidate']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillDetail
        exclude = ['candidate']
