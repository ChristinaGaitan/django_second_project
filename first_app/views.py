from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from first_app.forms import NewUserForm

# Create your views here.
def index(request):
  webpage_list = AccessRecord.objects.order_by('date')
  date_dictionary = {'access_records': webpage_list}
  return render(request, 'first_app/index.html', context=date_dictionary)

def users(request):
  user_list = User.objects.order_by('first_name')
  user_dictionary = { 'users': user_list }
  return render(request, 'first_app/users.html', context=user_dictionary)

def new_user(request):
  form = NewUserForm()
  if request.method == 'POST':
    form = NewUserForm(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return users(request)
    else:
      print('ERROR form invalid')
  return render(request,'first_app/new_user.html', {'form': form})
