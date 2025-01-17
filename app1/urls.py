from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('capture_student/', views.capture_student, name='capture_student'),
    path('', views.home, name='home'),
    path('selfie-success/', views.selfie_success, name='selfie_success'),
    path('capture-and-recognize/', views.capture_and_recognize, name='capture_and_recognize'),
    path('students/attendance/', views.student_attendance_list, name='student_attendance_list'),
    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/<int:pk>/authorize/', views.student_authorize, name='student-authorize'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('camera-config/', views.camera_config_create, name='camera_config_create'),
    path('camera-config/list/', views.camera_config_list, name='camera_config_list'),
    path('camera-config/update/<int:pk>/', views.camera_config_update, name='camera_config_update'),
    path('camera-config/delete/<int:pk>/', views.camera_config_delete, name='camera_config_delete'),
    path('bus-attendance/', views.bus_attendance, name='bus-attendance'),
    path('bus-attendance/toggle-status/<int:student_id>/', views.toggle_student_bus_status, name='toggle-student-bus-status'),
    path('bus/<int:bus_id>/add-student/', views.add_student_to_bus, name='add-student-to-bus'),
    path('bus/', views.bus_list, name='bus-list'),
    path('bus/create/', views.bus_create, name='bus-create'),
    path('bus/<int:pk>/edit/', views.bus_edit, name='bus-edit'),
    path('bus/<int:pk>/delete/', views.bus_delete, name='bus-delete'),
    path('bus/student/<int:student_id>/toggle-status/', views.toggle_student_bus_status, name='toggle-student-bus-status'),
    path('bus/<int:pk>/', views.bus_detail, name='bus-detail'),
    path('student/<int:student_id>/bus/<int:bus_id>/toggle/', views.toggle_student_bus_status, name='toggle-student-bus-status'),
    path('bus-tracking/', views.bus_tracking_list, name='bus-tracking'),
    path('bus-tracking/<int:bus_id>/', views.driver_tracking, name='driver-tracking'),
    path('driver-dashboard/', views.driver_dashboard, name='driver-dashboard'),
    path('driver-dashboard/<int:bus_id>/', views.driver_dashboard, name='driver-dashboard-detail'),
    path('update-driver-location/<int:bus_id>/', views.update_driver_location, name='update-driver-location'),
    path('get-bus-locations/', views.get_bus_locations, name='get-bus-locations'),
    path('update-bus-status/<int:bus_id>/', views.update_bus_status, name='update-bus-status'),
    path('get-student-status/<int:bus_id>/', views.get_student_status, name='get-student-status'),
    path('get-student-detail/<int:student_id>/', views.get_student_detail, name='get-student-detail'),
    path('bus-arduino-assign/', views.bus_arduino_assign, name='bus-arduino-assign'),
    path('get-arduino-ports-status/', views.get_arduino_ports_status, name='get-arduino-ports-status'),
]
    

