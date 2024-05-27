from django.shortcuts import get_object_or_404, render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost, Comment
from .forms import UserCommentModelForm
from .serializers import CommentSerializer
# from django.contrib.auth.models import User
# Create your views here.


def index(request):

    latest_blogs = BlogPost.objects.all()
    form = UserCommentModelForm()

    context = {
        'latest_blogs': latest_blogs,
        'form': form,
    }

    return render(request, 'index.html', context)


@csrf_exempt
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



