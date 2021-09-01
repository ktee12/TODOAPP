# from todolist.models import Todolist
from django.shortcuts import render
from .models import Todolist

# Create your views here.

def index(requst):
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(requst,'todolist/index.html', context)

