from email import message
from re import sub
from django.contrib.auth.models import User
from urllib import response
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Topic,Board,Post
# Create your views here.
# 
from .forms import NewTopicForm
from .models import Board
def home(request):

    boards=Board.objects.all()
    return render(  request=request,template_name='home.html',context={'boards':boards}) 
def boards_topics(request,id):
    # try :
    #    board=Board.objects.get(pk=id)
    # except Board.DoesNotExist:
    #     raise Http404
    board=get_object_or_404(Board,pk=id)


    return render(request=request,template_name='topics.html',context={'board':board})
def new_topic(request,id):
    board=get_object_or_404(Board,pk=id)
    form =NewTopicForm(request.POST)
    user=User.objects.first()
    
    


    if request.method=='POST':
        
        if form.is_valid():

            # print(form.cleaned_data['subject'])
            topic=form.save(commit=False)
            topic.board=board
            topic.created_by=user
            topic.save()
            print(topic)
 
      
            post=Post.objects.create(
                message=form.cleaned_data['message'],
                created_by=user,
                topic=topic
            )
            post.save()
            return redirect(to='board-topics',id=board.id)

       
    return render(request=request,template_name='newtopic.html',context={'board':board,'form':form} )    

        # topic=form.save(commit=False)
        # topic.board=board
        # topic.created_by=user
        # topic.save()
        # post=Post.objects.create(
        #     message=form.changed_data.get("message"),
        #     created_by=user,
        #     topic=topic
        # )
        # return redirect('board_topic',id=board.id)



    #     print('dddddddddddddddddddddddddddddddd')
       
        
    #     subject=request.POST['subject']
   
    #     message=request.POST['message']
    

    #     user=User.objects.first()
    #     topic=Topic(subject=subject,board_id=id,created_by=user)
    
    #     topic.save()

      
    #     post=Post(
    #         message=message,
    #         topic=topic,
    #         created_by=user



    #     )
    #     post.save()
        
    #     print('---------------------post-----------------')
    #     print(post)

    #     return redirect('board-topics',id=id)

