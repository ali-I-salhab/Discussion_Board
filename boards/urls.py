
from django.urls import path
from . import views
urlpatterns = [
    path('',view=views.home,name='home'),
    path('boards/<int:id>',view=views.boards_topics,name='board-topics'),
    path('boards/<int:id>/new',view=views.new_topic,name='new-topic'),

]
# dynamic link