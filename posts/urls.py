from unittest.mock import create_autospec
from venv import create
from django.urls import path

from posts.views import home_page, create_page, list_pages, update_page, view_page


urlpatterns = [
    # home page
    path('', home_page, name='home_page'),

    # create page url
    path('page/create_page', create_page, name='create_page'),

    # list pages
    path('page/list_pages/<int:id>/', list_pages, name='list_pages'),
    path('page/update_page/<int:id>/', update_page, name='update_page'),
    path('page/view_page/<int:id>/', view_page, name='view_page'),

]