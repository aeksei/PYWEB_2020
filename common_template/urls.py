from django.urls import path

from .views import SimpleView, JsonDatetimeView, SimpleTemplateView, DateTimeTemplateView
from .views import CreateBlogView, ListBlogView
urlpatterns = [
    path('simple/test/', SimpleView.as_view()),
    path('json_date/', JsonDatetimeView.as_view()),
    path('simple_template/', SimpleTemplateView.as_view()),
    path('datetime_template/', DateTimeTemplateView.as_view()),
    path('create_blog/', CreateBlogView.as_view()),
    path('list_blog/', ListBlogView.as_view()),
    path('list_blog/<int:pk>', ListBlogView.as_view()),
]
