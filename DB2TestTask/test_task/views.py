from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import ChooseSortForm, SearchForm
from .models import Post, PostComment


def posts_view(request):
    sort_form = ChooseSortForm
    search_form = SearchForm
    template_name = 'main.html'
    posts = Post.objects.order_by('author__city')
    if 'order_by' in request.POST:
        posted_sort_form = sort_form(request.POST)
        if posted_sort_form.is_valid():
            posts = Post.objects.order_by('author__' + request.POST['sort_by'])
    elif 'searchbtn' in request.POST:
        posted_search_form = search_form(request.POST)
        search_word = request.POST['search']
        if posted_search_form.is_valid():
            posts = Post.objects.filter(
                Q(title__istartswith=search_word) |
                Q(body__istartswith=search_word) |
                Q(author__city__istartswith=search_word) |
                Q(author__country__istartswith=search_word) |
                Q(author__email__istartswith=search_word))
    elif 'like_id' in request.POST and request.is_ajax():
        liked_post = Post.objects.get(id=request.POST['like_id'][0])
        if Post.objects.filter(likers=request.user).exists():
            liked_post.likers.remove(request.user)
            liked_post.save()
        else:
            liked_post.likers.add(request.user)
            liked_post.save()
        return JsonResponse({'likes_count': liked_post.likers.count()})
    paginated_posts = paginator(posts, request)
    return render(request, template_name, {
        'posts': paginated_posts,
        'sort_form': sort_form,
        'search_form': search_form})


def detail_post_view(request, post_id):
    template_name = 'detail_post.html'
    post = Post.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post)
    paginated_comments = paginator(comments, request)
    return render(request, template_name, {
        'post': post,
        'comments': paginated_comments})


def paginator(items, req):
    paginator = Paginator(items, 5)
    page = req.GET.get('page')
    try:
        paginated_items = paginator.page(page)
    except PageNotAnInteger:
        paginated_items = paginator.page(1)
    except EmptyPage:
        paginated_items = paginator.page(paginator.num_pages)
    return paginated_items
