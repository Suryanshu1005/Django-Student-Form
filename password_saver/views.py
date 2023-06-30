from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class CreateStudent(CreateView):
    model = Student
    fields = ['name', 'idNum', 'address', 'dept']
    success_url = reverse_lazy('student_list')


class UpdateStudent(UpdateView):
    model = Student
    fields = field = ['name', 'idNum', 'address', 'dept']
    success_url = reverse_lazy('student_list')

class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

