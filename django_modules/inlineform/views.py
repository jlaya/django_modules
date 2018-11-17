from django.shortcuts import render
from extra_views import NamedFormsetsMixin
from extra_views import UpdateWithInlinesView
from extra_views import InlineFormSet
from extra_views import CreateWithInlinesView
from .models import Invoice
from .models import InvoiceProduct


class InlineProductA(InlineFormSet):
    model = InvoiceProduct
    fields = '__all__'
    #factory_kwargs = {'extra': 4, 'max_num': 4}

class InlineProductB(InlineFormSet):
    model = InvoiceProduct
    fields = '__all__'
    #factory_kwargs = {'extra': 4, 'max_num': 4}

class CreateInvoice(NamedFormsetsMixin, CreateWithInlinesView):
    template_name = 'crud/create.html'
    model = Invoice
    success_url = reverse_lazy('list_course')
    inlines = [InlineProductA, InlineProductB]
    inlines_names = ['ProductA', 'ProductB']
    fields = '__all__'


class UpdateInvoice(NamedFormsetsMixin, UpdateWithInlinesView):
    template_name = 'chart/update.html'
    model = Invoice
    inlines = [InlineProductA, InlineProductB]
    inlines_names = ['ProductA', 'ProductB']
    fields = '__all__'