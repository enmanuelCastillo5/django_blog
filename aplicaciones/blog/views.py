from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Categoria
from django.core.paginator import Paginator
def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) |
        Q(descripcion__icontains = queryset)
        ).distinct()
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts':posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request,'post.html',{'detalle_post':post})


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Generales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Generales')
        )
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales.html', {'posts':posts})


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        )
    return render(request, 'programacion.html', {'posts':posts})


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Videojuego'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
        )
    return render(request, 'videojuegos.html', {'posts':posts})


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        )
    return render(request, 'tecnologia.html', {'posts':posts})


def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        )
    return render(request, 'tutoriales.html', {'posts':posts})