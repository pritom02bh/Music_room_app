from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    HttpResponse("<h1> Hello People! </h1>")
