from django.shortcuts import render, redirect

students_dict = {}


def student_list(request):
    return render(request, 'studentsapp/student_list.html', {'students': students_dict.items()})


def student_detail(request, student_id):
    student = students_dict.get(student_id)
    if student:
        return render(request, 'studentsapp/student_detail.html', {'student': student})
    else:
        return render(request, 'studentsapp/student_not_found.html')


def add_student(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        course = request.POST['course']
        age = request.POST['age']
        student_id = len(students_dict) + 1
        students_dict[student_id] = {'full_name': full_name, 'course': course, 'age': age}
        return redirect('student_list')
    return render(request, 'studentsapp/add_student.html')
