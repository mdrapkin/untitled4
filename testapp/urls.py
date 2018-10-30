from django.urls import path

from testapp.views import testview

urlpatterns = [
    path("hello/", testview)
]