from django.shortcuts import render

def post_list(request):
	return render('blog/post_list.html',{})
