from django.shortcuts import get_object_or_404, render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views import generic
from .models import BlogPost, Comment, Blogger
from .forms import UserCommentModelForm
from .serializers import CommentSerializer
from django.contrib.auth.models import User
from django.db.models import Count
# Create your views here.


@csrf_protect
def index(request):

    latest_blogs = BlogPost.objects.all()
    form = UserCommentModelForm()

    context = {
        'latest_blogs': latest_blogs,
        'form': form,
    }

    return render(request, 'index.html', context)

class BloggerListView(generic.ListView):
    model = Blogger
    # template_name = 'user_list.html'

    # def get_queryset(self):
    #     return Blogger.objects.filter(blogpost__isnull=False).distinct()
    


class BloggerDetailView(generic.DetailView):
    model = Blogger
    # template_name = 'blogger_detail.html'
    





@csrf_protect
def add_comment(request, blog_id):
    if request.method == "POST":
        # content = request.POST.get('comment')
        blogs = get_object_or_404(BlogPost, id=blog_id)

        form = UserCommentModelForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = blogs
            comment.comment_by = request.user
            comment.save()
            serializer = CommentSerializer(comment)
            return JsonResponse({'status': 'success', 'comment': serializer.data })
        else:
            return JsonResponse({'status': 'failure', 'errors': form.errors})

    return JsonResponse({'status': 'failure'})

        # print(request.user)

        # return HttpResponse(request, "hello")





