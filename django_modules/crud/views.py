from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.urls import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .models import Course


class ListCourse(PaginationMixin, ListView):
    template_name = 'crud/list.html'
    model = Course
    paginate_by = 10


class DetailCourse(DetailView):
    template_name = 'crud/detail.html'
    model = Course
    paginate_by = 1


class CreateCourse(CreateView):
    template_name = 'crud/create.html'
    model = Course
    success_url = reverse_lazy('list_course')
    fields = ['name', 'start_date', 'end_date']


class UpdateCourse(UpdateView):
    template_name = 'crud/update.html'
    success_url = reverse_lazy('list_course')
    model = Course
    fields = ['name', 'start_date', 'end_date']

    def get_success_url(self):
        return reverse('detail_course', kwargs={'pk': self.object.pk})


class DeleteCourse(DeleteView):
    template_name = 'crud/delete.html'
    model = Course
    success_url = reverse_lazy('list_course')
