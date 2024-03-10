from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from listapp.models import Todo
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

class Home(View):

    def get(self,request):
        context={}
        t=Todo.objects.filter(uid=request.user.id , iscompleted=False).count()
        print(t)
        task=Todo.objects.filter(uid=request.user.id)
        if len(task) != 0:
            context['data']=task
            context['task']=str(t)+" task are remaining...."
            return render(request,'list/index.html',context)
        else:
            context['nodata']="You have no task yet..."
            return render(request,'list/index.html',context)

    def post(self,request):
        context={}
        if request.user.is_authenticated:
            detail=request.POST['detail']
            # print(detail)
            if detail=='':
                context['errmsg']="Field cannot be empty"
                return render(request,'list/index.html',context)
            else:
                u_obj=User.objects.get(id=request.user.id)

                task=Todo.objects.create(detail=detail,uid=u_obj)
                task.save()
                return redirect('/')

        else:
            return redirect('accounts/login')
        
class Iscomp(View):
    def get(self,request,cid):
        c=Todo.objects.get(id=cid)
        cc=Todo.objects.filter(id=cid)

        if c.iscompleted==1:         
            cc.update(iscompleted=False)
            return redirect('/')
        
        else:
            cc.update(iscompleted=True)
            return redirect('/')
        
class Delete(View):
    def get(self,request,did):
        task=Todo.objects.filter(id=did)
        task.delete()
        return redirect('/')
    

class Sort(View):
    def get(self,request,sid):
        context={}
        sort_id=sid
        if request.user.is_authenticated:
            if sort_id == '1':
                q1=Q(uid=request.user.id)
                q2=Q(iscompleted=True)
                task=Todo.objects.filter(q1 & q2)
                context['data']=task
                return render(request,'list/index.html',context)
            
            elif sort_id == '2':
                q1=Q(uid=request.user.id)
                q2=Q(iscompleted=False)
                task=Todo.objects.filter(q1 & q2)
                context['data']=task
                return render(request,'list/index.html',context)
            
            else:
                task=Todo.objects.filter(uid=request.user.id)
                task.delete()
                return redirect('/')
        else:
            return redirect('/accounts/login')
