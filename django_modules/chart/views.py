from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from pure_pagination.mixins import PaginationMixin
from .models import Chart
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from django.urls import reverse_lazy
from django.shortcuts import render_to_response


class ChartList(PaginationMixin, ListView):
    template_name = 'chart/list.html'
    model = Chart
    paginate_by = 10


class ChartCreate(CreateView):
    template_name = 'chart/create.html'
    model = Chart
    success_url = reverse_lazy('chartlist_view')
    fields = ['name', 'start_date', 'end_date', 'type_chart', 'x_axis', 'y_axis']


class ChartDetail(DetailView):
    template_name = 'chart/detail.html'
    model = Chart
    paginate_by = 1


    def get_context_data(self, **kwargs):
        valorx = Chart.objects.values_list('x_axis').filter(pk=self.kwargs.get('pk'))
        valory = Chart.objects.values_list('y_axis').filter(pk=self.kwargs.get('pk'))
        eje_x = list(valorx)
        eje_y = list(valory)
        x_axis = list(eje_x[0])
        y_axis = list(eje_y[0])
        listx = ''.join(x_axis)
        listy = ''.join(y_axis)
        lx = listx.split(", ")
        ly = listy.split(", ")
        lx = list(map(int, lx))
        ly = list(map(int, ly))
        x = lx
        y = ly
        title = 'y = f(x)'
        plot = figure(title=title,
                      x_axis_label='X-Axis',
                      y_axis_label='Y-Axis',
                      plot_width=280,
                      plot_height=280
                      )
        plot.line(x, y, legend='f(x)', line_width=2)
        script, div = components(plot)
        return {'script': script, 'div': div}
