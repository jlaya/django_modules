from django.views.generic import ListView
from django.views.generic.detail import DetailView
from pure_pagination.mixins import PaginationMixin
from .models import Chart
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components


class ChartList(PaginationMixin, ListView):
    template_name = 'chart/list.html'
    model = Chart
    paginate_by = 10


class ChartDetail(DetailView):
    template_name = 'chart/detail.html'
    model = Chart
    paginate_by = 1

    # def get_context_data(self, **kwargs):
    #     x= [1,3,5,7,9,11,13]
    #     y= [1,2,3,4,5,6,7]
    #     title = 'y = f(x)'
    #     plot = figure(title= title , 
    #         x_axis_label= 'X-Axis', 
    #         y_axis_label= 'Y-Axis', 
    #         plot_width =400,
    #         plot_height =400)
    #     plot.line(x, y, legend= 'f(x)', line_width = 2)
    #     script, div = components(plot)
    #     context = super(ChartList, self).get_context_data(**kwargs)
    #     context['grafic'] = [script, div]
    #     print(context)
    #     return context
