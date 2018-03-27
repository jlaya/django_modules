from django.shortcuts import render
from wkhtmltopdf.views import PDFTemplateView
# Create your views here.
class WXHTMLTOPDF(PDFTemplateView):
    filename = 'wxhtmltopdf.pdf'
    template_name = 'wxhtmltopdf.html'
    cmd_options = {
        'margin-top': 3,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personas'] = OP_Person.objects.all()
        return context