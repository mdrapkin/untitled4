from django.http import HttpResponse
from django.shortcuts import render

from testapp.models import TestTable


def testview(request):
    #return HttpResponse("Hello World")
    test_table_object = TestTable.objects.first()
    return render(request, 'testapp/hello.html', {
        "test_table_object": test_table_object
    })
