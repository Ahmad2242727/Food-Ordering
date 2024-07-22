from home.models import Student
from vege.views import get_students, logout_page, register, login_tty, delete_receipe, receipe, see_marks, update_receipe
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from home.views import home

urlpatterns = [
    path('', login_tty ,name='home'),
    path('delete_receipes/<id>', delete_receipe,  name='delete_receipes'),
    path('update_receipes/<id>', update_receipe,  name='update_receipes'),
    path('receipes/', receipe ,  name='receipes'),
    path('register/', register,  name='register'),
    path('login/', login_tty  ,  name='login'),
    path('logout/', logout_page  ,  name='login_page'),
    path('admin/', admin.site.urls),
    path('students/', get_students ,  name='students'),
    path('see_marks/<student_id>/', see_marks ,  name='see_marks'),

]
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   