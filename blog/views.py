from django.shortcuts import render

def post_list(request):
    '''view for the page listing posts'''
    return render(request, 'blog/post_list.html', {})