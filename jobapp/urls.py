from django.urls import path
from jobapp import views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = "jobapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('jobs/', views.job_list_View, name='job-list'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    path('bookmark-job/<int:id>/', views.job_bookmark_view, name='bookmark-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/employer/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    path('dashboard/employer/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    path('dashboard/employer/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),
    path('dashboard/employer/close/<int:id>/', views.make_complete_job_view, name='complete'),
    path('dashboard/employer/delete/<int:id>/', views.delete_job_view, name='delete'),
    path('dashboard/employee/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),
     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('confirm-application/', views.send_application_confirmation_email, name='confirm_application'),
      path('video-interview/<int:id>/', views.video_interview, name='video_interview'),
    
    #  path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),


]
