from django.shortcuts import render
from extra_views import NamedFormsetsMixin
from extra_views import UpdateWithInlinesView
from extra_views import InlineFormSet
from extra_views import CreateWithInlinesView
from .models import Invoice
from .models import InvoiceProduct
from django.urls import reverse
from django.urls import reverse_lazy


class InlineProductA(InlineFormSet):
    model = InvoiceProduct
    fields = '__all__'
    factory_kwargs = {'extra': 1, 'max_num': 1}

class InlineProductB(InlineFormSet):
    model = InvoiceProduct
    fields = '__all__'
    factory_kwargs = {'extra': 1, 'max_num': 1}

class CreateInvoice(NamedFormsetsMixin, CreateWithInlinesView):
    template_name = 'inlineform/create.html'
    model = Invoice
    fields = '__all__'
    success_url = reverse_lazy('home')
    inlines = [InlineProductA, InlineProductB]
    inlines_names = ['ProductA', 'ProductB']


# class ChartCreate(CreateView):
#     form_class = ChartCreateForm
#     initial = {'key': 'value', 'type_chart': '1'}
#     success_url = reverse_lazy('chartlist_view')
#     template_name = 'chart/create.html'


#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             type_chart = form.cleaned_data['type_chart']
#             p = Chart()
#             p.name = name
#             p.type_chart = type_chart
#             p.owner = request.user
#             p.save()
#             return HttpResponseRedirect('/')
#         return render(request, self.template_name, {'form': form})    
    


class UpdateInvoice(NamedFormsetsMixin, UpdateWithInlinesView):
    template_name = 'inlineform/update.html'
    model = Invoice
    inlines = [InlineProductA, InlineProductB]
    inlines_names = ['ProductA', 'ProductB']
    fields = '__all__'