from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from .forms import UserRegisterForm, UserLoginForm, CreateStaffForm
from django.views.generic import CreateView, ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView, View
from .models import User, Agent, Manager
from django.contrib import messages


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
        # import pdb
        # pdb.set_trace()
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
        import pdb
        pdb.set_trace()
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
        # import pdb
        # pdb.set_trace()
        agent_list = Agent.objects.filter(manage_id=self.request.user.id)
        return agent_list
