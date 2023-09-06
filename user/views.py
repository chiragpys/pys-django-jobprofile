from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from .forms import UserRegisterForm, UserLoginForm, CreateStaffForm
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView, View
from .models import User, Agent, Manager
from django.contrib import messages
from candidate.models import CandidateProfile, ExperienceDetail


class UserCreateView(CreateView):
    template_name = 'user/register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:home')
    success_message = "User was create successfully."

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'home.html'


class LoginView(View):
    template_name = 'user/login.html'
    form_class = UserLoginForm

    def get(self, request):
        if request.session.get('user') is None:
            return render(request, self.template_name, {'form': self.form_class})
        else:
            return redirect('users:home')

    def post(self, request):
        if request.session.get('user') is None:
            form = self.form_class(request.POST)
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user = User.objects.get(username=user)
                if user.is_active == True:
                    request.session['user'] = username
                    login(request, user)
                    return redirect('users:home')
                else:
                    messages.error(request, "Your request is NOT approved")
            else:
                messages.error(request, "Username OR password is incorrect")
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('users:home')


# class LogoutView(View):
#     def get(self, request):
#         if request.session.get('user') is None:
#             return redirect('users:home')
#         else:
#             del request.session['user']
#             logout(request)
#             return redirect('users:home')


@method_decorator([never_cache], name='dispatch')
class logout_user(LogoutView):
    next_page = 'users:home'


class AssignManagerView(CreateView):
    template_name = 'page/managercreate.html'
    model = Manager
    fields = ['user']
    success_url = 'users:home'
    success_message = 'Manager Create successfully'

    def form_valid(self, form):
        user_id = form.instance.user_id
        if user_id:
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.is_manager = True
            user.save()
        return super().form_valid(form)


class ManagerList(ListView):
    template_name = 'page/manager_list.html'
    model = Manager


class AssignAgentView(CreateView):
    template_name = 'page/agent_assign.html'
    model = Agent
    fields = ['code', 'user']
    success_url = reverse_lazy('users:home')
    success_message = "Agent assign successful"

    def form_valid(self, form):
        form.instance.manage_id = self.request.user.id
        user_id = form.instance.user_id
        if user_id:
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.is_agent = True
            user.save()
        form.save()
        return super().form_valid(form)


class AgentList(ListView):
    template_name = 'page/agent_list.html'
    model = Agent

    def get_queryset(self):
        agent_list = Agent.objects.filter(manage_id=self.request.user.id)
        return agent_list


class CandidateRequestView(ListView):
    model = CandidateProfile
    template_name = 'page/candidate_request.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        # import pdb
        # pdb.set_trace()
        if self.request.user.is_manager:
            context['other'] = CandidateProfile.objects.filter(reference='other')
            context['all_agent_candidates'] = CandidateProfile.objects.filter(
                reference_details__in=self.request.user.manager.agent.all().values_list('code', flat=True))
            return context
        elif self.request.user.is_agent:
            context['candidates'] = CandidateProfile.objects.filter(reference_details=self.request.user.agent.code)
            return context


class download_file(View):
    def get(self, request, pk):
        file_download = ExperienceDetail.objects.filter(candidate__id=pk).first().resume
        if file_download.name == 'None':
            messages.error(request, 'No Resume Upload')
            return redirect('users:candidate-list')
        else:
            name = file_download.name.strip('documents/')
            response = HttpResponse(file_download.file, content_type='application/force-download')
            response['Content-Disposition'] = f'filename="{name}"'
            return response


class CandidateRequestUpdate(UpdateView):
    model = CandidateProfile
    template_name = 'page/candidate_profile_update.html'
    fields = ['profile_status']
    success_url = reverse_lazy("users:candidate-list")
    success_message = "Profile was Updated successfully"


class AdminShowRequest(ListView):
    template_name = 'page/admin_request.html'
    model = Manager

    def get_context_data(self, *, object_list=None, **kwargs, ):
        context = super().get_context_data()

        if self.request.user.is_superuser:
            context['managers'] = Manager.objects.all()
            return context


class AdminShowAgent(View):
    template_name = 'page/show_agent.html'
    model = Agent

    def get(self, request, pk):
        all_agent = Agent.objects.filter(manage_id=pk)
        return render(request, self.template_name, {'all_agent': all_agent})


class ShowAllRequestAdmin(View):
    template_name = 'page/show_all_agent_request_admin.html'

    def get(self, request, pk):
        candidates = CandidateProfile.objects.filter(
            reference_details__in=Agent.objects.filter(user_id=pk).values_list('code'))
        return render(request, self.template_name, {'candidates': candidates})


class AdminAllRequest(View):

    def get(self, request):
        manager_list = Manager.objects.filter().values_list('user_id', flat=True)
        agent_list = Agent.objects.filter(manage_id__in=manager_list).values_list('user_id', flat=True)
        agent_code = Agent.objects.filter(manage_id__in=manager_list).values_list('code', flat=True)
        candidates = CandidateProfile.objects.filter(reference_details__in=agent_code)


