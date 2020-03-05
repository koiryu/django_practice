from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from .forms import MyForm
from .models import Task

class TopPage(TemplateView):

    def __init__(self):
        self.params = {
            'title' : 'Hello',
            'message' : 'your data:',
            'form' : MyForm(),
            'data' : [],
        }
    def get(self, request):
        self.params['data'] = Task.objects.all()
        return render(request, 'TimeTrackTool/TopPage.html', self.params)

    def post(self, request):
        """
        msg = 'Your name is <b>' + request.POST['name'] + '(' + request.POST['age'] + ')</b>.<br>Your Mail is <b>' + request.POST['mail'] + '</b>.'  
        self.params['message'] = msg
        self.params['form'] = MyForm(request.POST)
        num = request.POST['id']
        item = Task.objects.get(id=num)
        self.params['data'] = [item]
        self.params['form'] = MyForm(request.POST)
        return render(request, 'TimeTrackTool/TopPage.html', self.params)
        """
        """
        Number = int(request.POST['Number'])
        TaskName = request.POST['TaskName']
        TimeStart = request.POST['TimeStart']
        TimeEnd = request.POST['TimeEnd']

        record = Task(Number=Number, TaskName=TaskName, TimeStart=TimeStart, TimeEnd=TimeEnd)
        record.save()
        return redirect(to='TimeTrackTool/TopPage')
        """
        obj = Task()
        record = MyForm(request.POST, instance=obj)
        record.save()
        return redirect(to='TimeTrackTool/TopPage')