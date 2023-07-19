from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import DemoContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response



class DemoContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = DemoContactSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = DemoContactSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)


from django.views.generic.base import TemplateView

class ExcelPageView(TemplateView):
    template_name= "excel_demo.html"



import xlwt
from django.http import HttpResponse
from .models import DemoContact
#from django.contrib.auth.models import User

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="usersdemo.xls"'


    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('DemoContact Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['title','number','organization','description', 'email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    # Sheet header, first row
    # Sheet header, first row
    font_style = xlwt.XFStyle()

    # Sheet header, first row
    rows =DemoContact.objects.all().values_list('title','number','organization','description', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

