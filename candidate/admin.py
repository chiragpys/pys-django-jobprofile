from django.contrib import admin
from .models import CandidateProfile, StudyDetail, ExperienceDetail, SkillDetail


# Register your models here.

class StudyInline(admin.StackedInline):
    model = StudyDetail
    extra = 1


class ExperienceInline(admin.StackedInline):
    model = ExperienceDetail
    extra = 1


class SkillInline(admin.StackedInline):
    model = SkillDetail
    extra = 1


class CandidateAdmin(admin.ModelAdmin):
    inlines = [StudyInline, ExperienceInline, SkillInline]
    search_fields = ('name',)
    list_filter = ('profile_status',)


admin.site.register(CandidateProfile, CandidateAdmin)
admin.site.register(StudyDetail)
admin.site.register(ExperienceDetail)
admin.site.register(SkillDetail)
