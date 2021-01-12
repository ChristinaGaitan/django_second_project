from django.shortcuts import render

# Create your views here.
def index(request):
  my_dictionary = { 'insert_content': 'hello I am from first app' }
  return render(request, 'first_app/index.html', context=my_dictionary)
