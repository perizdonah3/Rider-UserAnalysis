
from django.shortcuts import render, redirect, get_object_or_404
from closet.models import MyAppointments


# Home page
def home(request):
    return render(request, 'index.html')


# About Us
def about(request):
    return render(request, 'about.html')


# Burgundy Tops
def burgundy(request):
    return render(request, 'burgundy.html')


# Contact
def contact(request):
    return render(request, 'contact.html')


# Login
def login(request):
    return render(request, 'login.html')


# My Orders
def orders(request):
    return render(request, 'orders.html')


# Order Confirmation
def confirmation(request):
    return render(request, 'confirmation.html')


# Payment
def payment(request):
    return render(request, 'payment.html')


# Peach Tops
def peach(request):
    return render(request, 'peach.html')


# Privacy
def privacy(request):
    return render(request, 'privacy.html')


# Products
def products(request):
    return render(request, 'products.html')


# Profile
def profile(request):
    return render(request, 'profile.html')


# Register
def register(request):
    return render(request, 'register.html')


# Service and Reviews
def service(request):
    return render(request, 'service.html')


# Shop
def shop(request):
    return render(request, 'shop.html')


# Starter Page
def starter(request):
    return render(request, 'starter_page.html')


# Stripped Tops
def stripped(request):
    return render(request, 'stripped.html')


# Terms
def terms(request):
    return render(request, 'terms.html')


# Appointment page
def appointment(request):
    if request.method == 'POST':
        appointment = MyAppointments(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phonenumber=request.POST.get('phone'),
            datetime=request.POST.get('date'),
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        )

        appointment.save()
        return render(request, 'appointment.html')

    return render(request, 'appointment.html')


# Show all appointments
def show(request):
    allappointments = MyAppointments.objects.all()

    return render(
        request,
        'show.html',
        {'allappointments': allappointments}
    )


# Delete appointment
def delete(request, id):
    myappoint = get_object_or_404(MyAppointments, id=id)
    myappoint.delete()

    return redirect('/show')


# Edit appointment
def edit(request, id):
    editappointment = get_object_or_404(MyAppointments, id=id)

    if request.method == 'POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phonenumber = request.POST.get('phonenumber')
        editappointment.datetime = request.POST.get('datetime')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.message = request.POST.get('message')

        editappointment.save()

        return redirect('/show')

    return render(
        request,
        'edit.html',
        {'editappointment': editappointment}
    )