# # from django.shortcuts import render
# # from .forms import StudentForm

# # def start(request):
# #     if request.method == 'POST':
# #         fm = StudentForm(request.POST)
# #         if fm.is_valid():
# #             fm.save()
# #             fm = StudentForm() 
# #     else:
# #         fm = StudentForm()  
# #         stud=User.objects.all()  
# #     return render(request, 'add.html', {'form': fm,'stu':stud})


# # from django.shortcuts import render
# # from .forms import StudentForm
# # from .models import Stu

# # def start(request):
# #     if request.method == 'POST':
# #         form = StudentForm(request.POST)
# #         if form.is_valid():
# #             stud = form.save()
           
# #     else:
# #         form = StudentForm()
    
# #     stud = None  # Initialize stud to None to ensure it's always defined
    
# #     return render(request, 'add.html', {'form': form, 'stud': stud})

# from django.shortcuts import render, HttpResponseRedirect
# from .forms import StudentForm
# from .models import Stu

# def start(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to create a new Stu object
#              # Redirect to the same page to clear the form after submission
#     else:
#         form = StudentForm()

#     # Query all student records to display in the template
#     students = Stu.objects.all()

#     return render(request, 'add.html', {'form': form, 'students': students})

  
# def delete_data(request,id):
#     if request.method == 'POST':
#         pi=start.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Stu

def start(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start')
    else:
        form = StudentForm()

    students = Stu.objects.all()
    return render(request, 'add.html', {'form': form, 'students': students})

def delete_data(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Stu, pk=id)
        student.delete()
        return HttpResponseRedirect('/')

def update_data(request, id):
    pi = get_object_or_404(Stu, pk=id)
    if request.method == 'POST':
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('start')
    else:
        fm = StudentForm(instance=pi)
    
    return render(request, 'update.html', {'form': fm})




