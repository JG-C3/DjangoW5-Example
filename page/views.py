from django.shortcuts import render, redirect
# [코드 작성] models.py의 Post 모델 불러오기
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def read(request):
    # [코드 작성] Post 모델의 모든 객체를 리스트로 가져오기
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'page/read.html', context)

def create(request):
    # 만약 form에서 값을 전송하는 방식이 'POST'일 경우
    if request.method == 'POST':
        # [코드 작성] POST 방식으로 넘어온 값 중 'title'과 'content'의 값을 딕셔너리 형태로 반환
        title = request.POST.get('title')
        content = request.POST.get('content')

        # [코드 작성] Post 모델의 title과 content 필드값에 form으로 넘겨준 값을 저장하는 객체 생성
        Post.objects.create(
            title=title,
            content=content,
        )
        # 앱 이름이 'page'인 urls.py에서 name 속성값이 'read'인 url로 리다이렉트
        return redirect('page:read')
    else:
        return render(request, 'page/create.html')

def detail(request, id):
    # [코드 작성] Post 모델의 객체 중 id 값이 post_id와 같은 객체를 가져옴
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'page/detail.html', context)
