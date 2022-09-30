from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import PostModel


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'main/detail.html'


class CreateView(CreateView):
    model = PostModel
    template_name = 'main/create.html'
    fields = ['name', 'body', 'image']
    success_url = '/'


class HomeView(ListView):
    template_name = 'main/home.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search:
            qs = PostModel.objects.filter(name__icontains=search)
        else:
            qs = PostModel.objects.all().order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Abdulaziz'
        context['q'] = self.request.GET.get('search', '')
        return context


def home_view(request, id):
    posts = PostModel.objects.all()
    post = PostModel.objects.get(id=id)
    return render(request, 'main/home.html', context={
        'posts': posts,
        'title': 'hello',
        'post': post
    })
