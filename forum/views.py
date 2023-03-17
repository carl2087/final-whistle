from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, STATUS
from .forms import CommentForm, CreatePostForm
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from taggit.models import Tag


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        tags = Tag.objects.all()
        upvoted = False
        if post.up_votes.filter(id=self.request.user.id).exists():
            upvoted = True
        downvoted = False
        if post.down_votes.filter(id=self.request.user.id).exists():
            downvoted = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'upvoted': upvoted,
                'downvoted': downvoted,
                'comment_form': CommentForm(),
                'tags': tags
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        tags = Tag.objects.all()
        upvoted = False
        if post.up_votes.filter(id=self.request.user.id).exists():
            upvoted = True
        downvoted = False
        if post.down_votes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'upvoted': upvoted,
                'downvoted': downvoted,
                'comment_form': CommentForm(),
                'tags': tags
            },
        )


class PostUpvote(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.up_votes.filter(id=request.user.id).exists():
            post.up_votes.remove(request.user)
        else:
            post.up_votes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostDownvote(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.down_votes.filter(id=request.user.id).exists():
            post.down_votes.remove(request.user)
        else:
            post.down_votes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(View):
    form_class = CreatePostForm
    initial = {'key': 'value'}
    template_name = 'create_post.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.title)
            create = form.save()
            return render(
                request,
                'create_post.html',
                {
                    'posted': True,
                }
            )
        else:
            return render(
                request,
                'create_post.html',
                {
                    'form': form,
                    'failed': True,
                    'posted': False,
                }
            )


class EditPost(TemplateView):
    model = Post
    template_name = 'edit_post.html'

    def get(self, request, pk, *args, **kwargs):
        forum_post = Post.objects.get(pk=pk)
        form = CreatePostForm(instance=forum_post)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'posted': False
            }
        )

    def post(self, request, pk, *args, **kwargs):

        forum_post = Post.objects.get(pk=pk)
        form = CreatePostForm(request.POST, request.FILES, instance=forum_post)

        if form.is_valid():
            form.instance.slug = slugify(form.instance.title)
            form.save()

        return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'posted': True
                }
            )


class MyPosts(generic.ListView):

    model = Post
    template_name = 'my_posts.html'

    def get(self, request):

        queryset = Post.objects.filter(
            author=request.user.id).order_by('-created_on')
        queryset_dict = {
            'my_posts': queryset
        }

        return render(
            request,
            self.template_name,
            queryset_dict,
        )


class DeletePost(View):

    def get(self, request, pk, *args, **kwargs):

        post = get_object_or_404(Post, pk=pk)
        post.delete()

        return redirect(reverse('my_posts'))