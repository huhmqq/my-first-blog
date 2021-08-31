from django.shortcuts import render

def post_list(request):
    return render(request, 'gamesfold/post_list.html', {})