from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from .forms import MyForm

class TopPage(TemplateView):

    def __init__(self):
        self.params = {
            'title' : 'Hello',
            'message' : 'your data:',
            'form' : MyForm()
        }
    def get(self, request):
        return render(request, 'TimeTrackTool/TopPage.html', self.params)

    def post(self, request):
        msg = 'Your name is <b>' + request.POST['name'] + '(' + request.POST['age'] + ')</b>.<br>Your Mail is <b>' + request.POST['mail'] + '</b>.'  
        self.params['message'] = msg
        self.params['form'] = MyForm(request.POST)
        return render(request, 'TimeTrackTool/TopPage.html', self.params)