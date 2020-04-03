from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View  # 原书没有
# Create your views here.
def index(request):
    # words = '贺虎'
    # return render(request, 'index.html', context={'words': words})
    students = Student.objects.all()   # 获取所有student数据
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save()
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }

    return render(request, 'index.html', context=context)

class IndexView(View):
    template_name = 'index.html'

    # 获取学员信息
    def get_context(self):
        students = Student.get_all()    # 使用model中定义的类方法
        context = {
            'students': students,
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()    # 创建form对象
        context.update({
            'form': form,
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        # 接受form表单提交的数据
        form = StudentForm(request.POST)
        if form.is_valid() :
            form.save()
            # 重定向，使用reverse方法反向解析url地址，也可用redirect方法重定向
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        # 走到这则证明form表单数据异常，此时form中会带上错误信息，如qq号格式错误，邮箱格式错误等
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
