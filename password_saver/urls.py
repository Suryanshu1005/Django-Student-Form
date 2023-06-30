from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.StudentList.as_view(), name='student_list'),
    path('view/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('new', views.CreateStudent.as_view(), name='student_new'),
    path('edit/<int:pk>', views.UpdateStudent.as_view(), name='student_edit'),
    path('delete/<int:pk>', views.DeleteStudent.as_view(), name='student_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
