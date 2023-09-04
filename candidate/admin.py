from django.contrib import admin
from .models import CandidateProfile, StudyDetail, ExperienceDetail, SkillDetail

# Register your models here.
admin.site.register(CandidateProfile)
admin.site.register(StudyDetail)
admin.site.register(ExperienceDetail)
admin.site.register(SkillDetail)
