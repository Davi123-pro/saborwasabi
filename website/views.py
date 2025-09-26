# website/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Comment, Contact
from .forms import ContactForm

def home(request):
    return render(request, 'website/home.html')

def team(request):
    return render(request, 'website/team.html')

def contact(request):
    """
    Renderiza e processa o formulário de contato.
    Se o form for válido, salva no banco (Contact) e mostra mensagem de sucesso.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato.')
            return redirect('contact')
        else:
            messages.error(request, 'Por favor corrija os erros no formulário.')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def posts_list(request):
    posts = Post.objects.all()
    for p in posts:
        p.comments_count = p.comments.count()
    return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            post.likes_count = (post.likes_count or 0) + 1
            post.save()
            return redirect('post_detail', slug=post.slug)
        elif action == 'comment':
            name = request.POST.get('name', 'Anônimo')
            text = request.POST.get('text')
            if text:
                Comment.objects.create(post=post, name=name, text=text)
            return redirect('post_detail', slug=post.slug)

    return render(request, 'blog/post_detail.html', {'post': post})
