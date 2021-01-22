from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', home, name='signup'),
    path('signup/<str:plan_subscribed>', sign_up, name='signup'),
    path('signin/', sign_in, name='signin'),
    path('signout/', sign_out, name='signout'),
    path('checkout/', checkout_page, name='checkout_page'),
    path('sybadmin/', syb_admin_page, name='syb_admin_page'),
    path('college/', college_page, name='college_page'),
    path('college/add_teachers', college_add_teachers, name='college_add_teachers'),
    path('college/add_teachers/<int:pk>', college_add_teachers, name='college_add_teachers'),
    path('college/del_teachers/<int:pk>', college_del_teachers, name='college_del_teachers'),
    path('college/add_classes', college_add_classes, name='college_add_classes'),
    path('college/add_classes/<int:pk>', college_add_classes, name='college_add_classes'),
    path('college/del_classes/<int:pk>', college_del_classes, name='college_del_classes'),
    path('college/teacher', college_teacher, name='college_teacher'),
    path('college/teacher/add_subjects', college_teacher_add_subjects, name='college_teacher_add_subjects'),
    path('college/teacher/add_subjects/<int:pk>', college_teacher_add_subjects, name='college_teacher_add_subjects'),
    path('college/teacher/add_students', college_teacher_add_students, name='college_teacher_add_students'),
    path('college/teacher/add_students/<int:pk>', college_teacher_add_students, name='college_teacher_add_students'),
    path('college/teacher/update_students/<int:pk>', college_teacher_update_students, name='college_teacher_update_students'),
    path('college/teacher/view_student_lists', view_student_lists, name='view_student_lists'),
    path('college/teacher/classroom/<int:pk>', college_teacher_classroom, name='college_teacher_classroom'),
    path('college/teacher/classroom/<int:pk>/add_post', college_teacher_classroom_add_post, name='college_teacher_classroom_add_post'),
    path('college/teacher/classroom/view_test/<int:pk>', college_teacher_classroom_view_test, name='college_teacher_classroom_view_test'),
    path('college/teacher/classroom/delete_test/<int:pk>', college_teacher_classroom_delete_test, name='college_teacher_classroom_delete_test'),
    path('college/teacher/classroom/view_tests_submissions/<int:class_pk>', view_tests_submissions, name='view_tests_submissions'),
    path('college/teacher/classroom/view_assignments_submissions/<int:class_pk>', view_assignments_submissions, name='view_assignments_submissions'),
    path('college/teacher/classroom/view_test_performance/<int:pk>', view_test_performance, name='view_test_performance'),
    path('college/student', college_student, name='college_student'),
    path('college/student/classroom/college_student_assignments', college_student_assignments, name='college_student_assignments'),
    path('college/student/classroom/college_student_submit_assignment/<int:pk>', college_student_submit_assignment, name='college_student_submit_assignment'),
    path('college/student/classroom/college_student_reading_materials', college_student_reading_materials, name='college_student_reading_materials'),
    path('college/student/classroom/college_student_videos', college_student_videos, name='college_student_videos'),
    path('college/student/classroom/college_student_articles', college_student_articles, name='college_student_articles'),
    path('college/student/classroom/give_test/<int:pk>', college_student_classroom_give_test, name='college_student_classroom_give_test'),
    path('college/classroom/view_post/<int:pk>', college_student_classroom_view_post, name='college_student_classroom_view_post'),
    path('college/classroom/comment', college_classroom_post_comment, name='college_classroom_post_comment'),
    path('college/classroom/reply', college_classroom_post_reply, name='college_classroom_post_reply'),
]
