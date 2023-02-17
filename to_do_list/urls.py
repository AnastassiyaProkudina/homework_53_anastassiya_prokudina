from django.urls import path

from to_do_list.views.base import index_view
from to_do_list.views.tasks import add_view, detail_view, delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('task/', index_view),
    path('task/add', add_view, name='task_add'),
    path('task/<int:pk>', detail_view, name='task_detail'),
    path('task/delete/<int:pk>', delete_view, name='task_delete')
]
