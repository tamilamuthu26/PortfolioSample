from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def index(request):
    form = ContactForm()  # Initialize the form for GET requests
    return render(request, 'index.html', {'form': form})

def addnew(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the model
            messages.success(request, 'Your message has been submitted successfully!')
            return redirect('/')  # Redirect after successful form submission
    else:
        form = ContactForm()  # Reinitialize the form for GET requests
    return render(request, 'index.html', {'form': form})
