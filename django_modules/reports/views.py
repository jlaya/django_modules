from django.views.generic import TemplateView
from wkhtmltopdf.views import PDFTemplateView
from django_modules.home.models import Products
# from django.views.generic.detail import SingleObjectMixin
# from django.views.generic import View
# from wkhtmltopdf.views import PDFTemplateResponse


class ReportsView(TemplateView):
    template_name = "reports/index.html"


class Wkhtmltopdf(PDFTemplateView):
    filename = 'wkhtmltopdf.pdf'
    template_name = 'reports/wkhtmltopdf.html'
    footer_template = 'reports/footer.html'
    cmd_options = {
        'margin-top': 3,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context

# PDF con 2 modelos relacionados
# class PurchasePDF(PDFTemplateView, SingleObjectMixin):
#     filename = 'my_pdf.pdf'
#     template_name = 'purchases/purchase/purchasepdf.html'
#     cmd_options = {
#         'margin-top': 3,
#     }

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Purchase.objects.all())
#         return super(PurchasePDF, self).get(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super(PurchasePDF, self).get_context_data(**kwargs)
#         context['purchase'] = self.object
#         context['lista_products'] = PurchaseDetail.objects.filter(
#                                                 relationship=self.object.pk)
#         return context

# Otra forma de usar wkhtmltopdf
# class WKXHTMLTOPDF(View):
#     filename = 'wkxhtmltopdf.pdf'
#     template = 'wkxhtmltopdf.html'
#     cmd_options = {
#         'margin-top': 10,
#         'orientation': 'landscape',
#     }
#     context = {}

#     def post(self, request, *args, **kwargs):
#         org = OC_Organization.objects.all()[0]
#         org.image = _settings.BASE_DIR + '/' + org.image
#         table = None
#         if request.method == 'POST':
#             report = OR_Report.objects.get(id=int(request.POST['report']))
#             headers = [i.model_field.name for i in OR_ReportFieldToShow.
#                        objects.filter(
#                            status=True,
#                            report=report
#                        ).exclude(
#                            Q(model_field__field_name='description') |
#                            Q(model_field__field_name='content')
#                        ).order_by('position')]

#             field_names = [i.model_field.field_name.replace('_id', '') if (
#                 i.model_field.field_name != 'conversion_object_id_record') else (
#                     i.model_field.field_name)
#                         for i in OR_ReportFieldToShow.objects.
#                         filter(report_id=report, status=True).exclude(
#                             Q(model_field__field_name='description') |
#                             Q(model_field__field_name='content')
#                         ).order_by('position')]

#             is_total = json.loads(request.POST['isTotal'])

#             if is_total:
#                 data = json.loads(request.POST['total_data'])[1:]
#                 headers = json.loads(request.POST['total_data'])[0]
#                 table = request.POST['table']
#             else:
#                 data = get_report_query(
#                     request.POST['model'],
#                     json.loads(request.POST['params']),
#                     json.loads(request.POST['fields']),
#                     json.loads(request.POST['isTotal']),
#                     True)

#         return PDFTemplateResponse(
#             request=request,
#             context={
#                 'pagesize': 'A4 landscape',
#                 'org': org,
#                 'title': report.name,
#                 'field_names': field_names,
#                 'headers': headers,
#                 'data': data,
#                 'table': table,
#                 'is_total': is_total
#             },
#             template=self.template,
#             filename=self.filename,
#             show_content_in_browser=True,
#             cmd_options=self.cmd_options)
