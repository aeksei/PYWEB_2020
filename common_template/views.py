from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Blog
from . serializers import blog_to_json
# Create your views here.


class SimpleView(View):
    def get(self, request):
        html = """<h1>Hello, World</h1>"""
        return HttpResponse(html)


class JsonDatetimeView(View):
    def get(self, request):
        now = datetime.now()
        dict_ = {
            'day': now.day,
            'month': now.month,
            'year': now.year,
        }

        return JsonResponse(dict_, json_dumps_params={"indent": 4})


class SimpleTemplateView(View):
    def get(self, request):
        return render(request,
                      "common_template/index.html")


class DateTimeTemplateView(View):
    def get(self, request):
        now = datetime.now()
        context = {
            'day': now.day,
            'month': now.month,
            'year': now.year,
            'second': now.second
        }
        return render(request,
                      "common_template/datetime.html",
                      context=context)


class CreateBlogView(View):
    def get(self, request):
        # /create_blog/?title=tmp
        blog = Blog(
            title=request.GET['title'],
        )

        blog.save()

        return render(request,
                      "common_template/create.html",
                      context={'blog': blog}
                      )


class ListBlogView(View):
    def get(self, request, pk=None):
        if pk is None:
            blogs = Blog.objects.all()
            return JsonResponse([blog_to_json(blog)
                                 for blog in blogs],
                                safe=False,
                                json_dumps_params={"indent": 4})

        else:
            blog = get_object_or_404(Blog, pk=pk)
            return render(request,
                          "common_template/create.html",
                          context={'blog': blog}
                          )



