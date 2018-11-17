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
    


class UpdateInvoice(NamedFormsetsMixin, UpdateWithInlinesView):
    template_name = 'inlineform/update.html'
    model = Invoice
    inlines = [InlineProductA, InlineProductB]
    inlines_names = ['ProductA', 'ProductB']
    fields = '__all__'