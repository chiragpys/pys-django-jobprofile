from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.

class CreateCandidateProfile(CreateView):
    template_name = 'form.html'
    success_url = reverse_lazy('candidate:form')
    form_class = CandidateProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['candidate_experience'] = ExperienceForm()
        context['candidate_study'] = StudyForm()
        context['candidate_skill'] = SkillForm()
        return context

    def form_valid(self, form):

        candidate = form.save()
        candidate_study = self.get_form(form_class=StudyForm)
        candidate_study.instance.candidate_id = candidate.id
        candidate_experience = self.get_form(form_class=ExperienceForm)
        candidate_experience.instance.candidate_id = candidate.id
        candidate_skill = self.get_form(form_class=SkillForm)
        candidate_skill.instance.candidate_id = candidate.id
        if candidate_study.is_valid() and candidate_experience.is_valid() and candidate_skill.is_valid():

            if candidate_study.instance.school != None:
                candidate_study.save()
            if candidate_experience.instance.company != None:
                candidate_experience.save()
            if candidate_skill.instance.technical != None and candidate_skill.instance.language != None:
                candidate_skill.save()
        return super().form_valid(form)
