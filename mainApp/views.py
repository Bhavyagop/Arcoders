from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from openpyxl import load_workbook, workbook


def login(request):
    form = CreateUserForm()

    if request.method == 'POST' and 'register_form' in request.POST:
        if request.user.authenticated:
            return redirect('home')
        else:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
    
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request)
            return redirect('home')

        else:
            messages.info(request, "Username or password is incorrect.")

    context = {'form' : form}
    return render(request, "login.html", context)


def log_out(request):
    return redirect("/")


def coming_soon(request):
    return render(request, 'coming_soon.html')

# @login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        event_date = request.POST.get('event_date')
        entry_date = request.POST.get('entry_date')
        department = request.POST.get('department')
        attendees = request.POST.get('attendees')
        link = request.POST.get('link')
        email = request.POST.get('email')

        # Open the excel file
        wb_name = "hackathon"
        path = '/home/kaushalk/development/hackathon /hackathon.xlsx'
        wb = load_workbook(path, read_only=False, keep_vba=True)
        sheet = wb.active

        # Insert the data into the excel sheet
        print(name, event_date, entry_date, department, attendees, link, email)
        sheet.append([name, event_date, entry_date, department, attendees, link, email])

        # Save the excel file
        wb.save("hackathon.xlsx")

    return HttpResponse("Success")


def download_xlsx(request):
    # the path to the .xlsx file on your server
    file_path = 'hackathon.xlsx'
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=hackathon.xlsx'
    return response


def preview_xlsx(request):
    # the path to the .xlsx file on your server
    file_path = 'hackathon.xlsx'
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'inline; filename=hackathon.xlsx'
    return response