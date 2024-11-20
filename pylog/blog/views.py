from django.shortcuts import render , redirect
from blog.models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all() # 모든 post 객체를 가진 쿼리셋
    context = {
        'posts' : posts,
    }
    return render (request, 'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create( #comment 객체 생성 
            post=post,
            content = comment_content,
        )
    context = { "post" : post,}
    return render(request, 'post_detail.html', context)

def post_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]
        post = Post.objects.create(
            title = title,
            content = content,
            thumbnail = thumbnail,
        )
        return redirect(f"/posts/{post.id}/") # GET 처음 페이지 호출 
    else:
        print(request.method)
    return render(request, "post_add.html")
