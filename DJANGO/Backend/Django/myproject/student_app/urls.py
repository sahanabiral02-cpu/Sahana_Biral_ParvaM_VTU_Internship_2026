urlpatterns = [
    path('', views.student_list, name="list_of_students"),
    path('form/', views.student_form, name="registration_form"),
    path('info/', views.student_info, name="student_details"),
    path('<int:pk>/', views.student_info, name="student_details"),
    path('<int:pk>/edit', views.edit_student, name="update_details"),
    path('<int:pk>/delete', views.delete_student, name="remove_student"),