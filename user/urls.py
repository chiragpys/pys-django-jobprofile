from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('register', UserCreateView.as_view(), name='register'),
    path('home', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', logout_user.as_view(), name='logout'),
    path('managerCreate', AssignManagerView.as_view(), name='managerCreate'),
    path('manager-list', ManagerList.as_view(), name='manager-list'),
    path('agent-assign', AssignAgentView.as_view(), name='agent-assign'),
    path('agent-list', AgentList.as_view(), name='agent-list'),
    path('candidate', CandidateRequestView.as_view(), name='candidate-list'),
    path('download/<int:pk>', download_file.as_view(), name='download'),
    path('candidate/update/<int:pk>', CandidateRequestUpdate.as_view(), name='candidate-update'),

    # path('admin-show-request/', AdminShowRequest.as_view(), name='admin-show-request'),
    # path('allagentshow/<int:pk>', AdminShowAgent.as_view(), name='All-agent'),
    # path('allrequest-agent/<int:pk>', ShowAllRequestAdmin.as_view(), name='allrequest-agent')

    path('admin-show-request/', AdminAllRequest.as_view(), name='admin-show-request'),

]
