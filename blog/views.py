from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	form = PostForm()

	if request.method == "POST": #method will be POST if we have used the post_edit.html template.
		form = PostForm(request.POST)		
	
		if form.is_valid(): #Check to make sure the form is valid
			post = form.save(commit=False) #commit=False because we don't want to save the Post model yet.
			post.author = request.user
			post.published_date = timezone.now()
			post.save() #now since the author and published date have been added, we can save the Post model.
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	

	return render(request, 'blog/post_edit.html', {'form':form})

