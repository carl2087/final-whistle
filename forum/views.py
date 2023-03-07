from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        if post.up_votes.filter(id=self.request).exists():
            upvoted = True
        downvoted = False
        if post.down_votes.filter(id=self.request).exists():
            downvoted = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'upvoted': upvoted,
                'downvoted': downvoted
            }
        )
