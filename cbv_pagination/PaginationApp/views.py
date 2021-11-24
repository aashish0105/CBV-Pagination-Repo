from django.views.generic import ListView
from .models import Posts
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


class PostsListViewGen(ListView):
    paginate_by = 10
    model = Posts
    template_name = 'PaginationApp/display_posts.html'
    context_object_name = "posts_objs"


class PostsListView(ListView):
    paginate_by = 5
    model = Posts
    template_name = 'PaginationApp/display_posts1.html'

    def get_context_data(self,**kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        posts = Posts.objects.all()
        paginator = Paginator(posts, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            posts_page = paginator.page(page)
        except PageNotAnInteger:
            posts_page = paginator.page(1)
        except EmptyPage:
            posts_page = paginator.page(paginator.num_pages)

        context['posts_objs'] = posts_page
        return context


