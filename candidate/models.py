from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CandidateProfile(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    dob = models.DateField(_("Date of birth"))
    gender = models.CharField(_("Gender"), max_length=10, default="Male", choices=Gender)
    mobile_no = models.CharField(_("Mobile No"), max_length=10)
    email = models.EmailField(_("Email Id"), max_length=100, unique=True)
    created = models.DateField(auto_now=True)
    address = models.TextField(_("Address"), null=True, blank=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name


class StudyDetail(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='study')
    school = models.CharField(_("School/College"), max_length=200, null=True, blank=True)
    standard = models.CharField(_("Standard Name"), max_length=100, null=True, blank=True)
    percentage = models.FloatField(_("Percentage %"), null=True, blank=True)
    passing_year = models.DateField(_("Passing Year"), null=True, blank=True)
    upload_documents = models.FileField(upload_to='documents', null=True, blank=True)

    def __str__(self):
        return f"{self.school}"


class ExperienceDetail(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(_("Company Name"), max_length=200, null=True, blank=True)
    titel = models.CharField(_("Job Title"), max_length=100, null=True, blank=True)
    start_date = models.DateField(_("Join date"), null=True, blank=True)
    end_date = models.DateField(_("End date"), null=True, blank=True)
    discription = models.TextField(_("Job discription "), null=True, blank=True)

    def __str__(self):
        return f"{self.company}"


class SkillDetail(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='skills')
    technical = models.TextField(_("Technical Skills"), null=True, blank=True)
    soft = models.TextField(_("Soft Skills"), null=True, blank=True)
    project = models.TextField(_("Project Details"), null=True, blank=True)
    language = models.TextField(_("Language Know"), null=True, blank=True)
    certificate = models.FileField(_('Certificate'), upload_to='documents', null=True, blank=True)

    def __str__(self):
        return f"{self.candidate} Skills"
