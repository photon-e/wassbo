from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'store/index.html', {'home_view': home_view})
