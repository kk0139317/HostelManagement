from home import views
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='home' ),
    path('profile', views.profile, name='profile' ),
    path('hostel', views.hostel, name='hostel' ),
    path('enquiry', views.enquiry, name='enquiry' ),
    path('mess', views.mess, name='mess' ),
    path('outing', views.outing, name='outing' ),
    path('leave', views.leave, name='leave' ),
    path('add-new', views.add_new, name='add_new' ),
    path('add-admin', views.add_admin, name='add-admin' ),
    path('add-student', views.add_student, name='add-student' ),
    path('breakfast', views.breakfast, name='breakfast' ),
    path('complain', views.complain, name='complain' ),
    path('dinner', views.dinner, name='dinner' ),
    path('enquiry', views.enquiry, name='enquiry' ),
    path('g-floor', views.g_floor, name='g-floor' ),
    path('girls-hostel', views.girls_hostel, name='girls-hostel' ),
    path('green-hostel', views.green_hostel, name='green-hostel' ),
    path('hostel-1', views.hostel_1, name='hostel-1' ),
    path('hostel-2', views.hostel_2, name='hostel-2' ),
    path('hostel-3', views.hostel_3, name='hostel-3' ),
    path('hostel', views.hostel, name='hostel' ),
    path('lunch', views.lunch, name='lunch' ),
    path('manage-admin', views.manage_admin, name='manage-admin' ),
    path('manage-student', views.manage_student, name='manage-student' ),
    path('room-change', views.room_change, name='room-change' ),
    path('update-admin', views.update_admin, name='update-admin' ),
    path('login', views.loginuser, name='login' ),
    path('logout', views.logoutuser, name='logout' ),
    path('student-index', views.student_index, name='student_index' ),
    path('student-outing', views.student_outing, name='student_outing' ),
    path('student-profile', views.student_profile, name='student_profile' ),
    path('student-leave', views.student_leave, name='student_leave' ),
    # path('student-leave-aproval/<str:leave_id>', views.student_leave_aproval, name='student-leave-aproval' ),
    path('leave_accept/<int:pid>', views.leave_accept, name = 'leave_accept'),
    path('leave_reject/<int:pid>', views.leave_reject, name = 'leave_reject'),
    path('outing_accept/<int:pid>', views.outing_accept, name = 'outing_accept'),
    path('outing_reject/<int:pid>', views.outing_reject, name = 'outing_reject'),
    path('student-leave-status', views.student_leave_status, name='student_leave_status'),
    path('student-outing-status', views.student_outing_status, name='student_outing_status'),
    path('student-enquiry', views.student_enquiry, name='student-enquiry'),
    path('student-room-change', views.student_room_change, name='student-room-change'),
    path('student-complain', views.student_complain, name='student-complain'),
    path('room-change-accept/<int:pid>', views.room_change_aproved, name = 'room-change-accept'),
    path('room-change-decline/<int:pid>', views.room_change_decline, name = 'room-change-decline'),
    path('complain_delete/<int:pid>', views.complain_delete, name = 'complain_delete'),
    path('chat_student', views.chat_student, name='chat_student'),
    path('student-list', include('home.student_url')),
    # path('student-list-1500', views.student_list, name='stuednt_list'),
    path('student-mess', views.student_mess, name='student_mess' ),
    path('student-breakfast', views.student_breakfast, name='student_breakfast'),
    path('student-lunch', views.student_lunch, name='student_lunch'),
    path('student-dinner', views.student_dinner, name='student_dinner' ),
      
     
    
]
