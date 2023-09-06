from django import forms
from .models import CandidateProfile, SkillDetail, ExperienceDetail, StudyDetail


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = [
            'name',
            'last_name',
            'dob',
            'gender',
            'mobile_no',
            'email',
            'reference',
            'reference_details',
            'address',
            'photo'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'created': forms.DateInput(attrs={'type': 'date'})
        }


class StudyForm(forms.ModelForm):
    class Meta:
        model = StudyDetail
        fields = [
            'school',
            'standard',
            'percentage',
            'passing_year',
            'upload_documents'
        ]
        widgets = {
            'passing_year': forms.DateInput(attrs={'type': 'date'}),
        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        fields = [
            'company',
            'titel',
            'start_date',
            'end_date',
            'discription',
            'resume',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillDetail
        fields = [
            'technical',
            'soft',
            'project',
            'language',
            'certificate'
        ]
