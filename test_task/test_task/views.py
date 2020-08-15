from django.shortcuts import render, get_object_or_404, get_list_or_404




def get_central_page(request):
    return render(request, 'index.html')