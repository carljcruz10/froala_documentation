from django.shortcuts import redirect, render

from posts.models import Article, Page
from posts.forms import ArticleForm, PageForm


def home_page(request):
    template_name = 'homepage.html'

    # query the articles and posts for the homepage
    articles = Article.objects.all()
    posts = Page.objects.all()
    context = {
        'articles': articles,
        'posts': posts
    }
    return render(request, template_name, context=context)


# Articles
def create_article(request):
    form = ArticleForm(request.POST or None)
    template_name = 'create_article'
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(home_page)

    context = {
        'form': form,
    }
    return render(request, template_name, context=context)

def update_article(request,id):
    get_article = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None)
    template_name = 'update_article.html'
    context = {
        'article': get_article,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(view_article, id)
    return render(request, template_name, context=context)

def view_article(request, id):
    get_article = Article.objects.get(id=id)
    template_name = 'view_article.html'

    context = {
        'article': get_article,
    }
    return render(request, template_name, context=context)

def delete_article(request, id):
    get_article = Article.objects.get(id=id)
    get_article.delete()
    return redirect(home_page)


# Pages 
def create_page(request):
    form = PageForm(request.POST or None)
    template_name = 'create_page.html'
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(home_page)

    context = {
        'form': form,
    }
    return render(request, template_name, context=context)

def update_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)

    # populate it with the instance
    form = PageForm(request.POST or None, instance=get_page)
    template_name = 'update_page.html'
    
    if request.method == 'POST':
        if form.is_valid():
            # save the form
            form.save()
            return redirect(view_page, id)

    context = {
        'page': get_page,
        'form': form,
    }
    return render(request, template_name, context=context)

def view_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)
    template_name = 'view_page.html'

    # get the related pages
    related_pages = Page.objects.filter(article=get_page.article).exclude(id=id)

    context = {
        'page': get_page,
        'related_pages': related_pages,
    }
    return render(request, template_name, context=context)

def delete_page(request, id):
    # get page
    get_page = Page.objects.get(id=id)

    # delete the page
    get_page.delete()
    return redirect(home_page)



def list_pages(request, id):
    template_name = 'list_pages.html'
    # get the article
    get_article = Article.objects.get(id=id)
    pages = Page.objects.filter(article=get_article)
    context = {
        'pages': pages,
    }
    return render(request, template_name, context=context)