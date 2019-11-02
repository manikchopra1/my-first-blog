from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('home')
    else :
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form' : form})

def profile(request):
    if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

            if form.is_valid():
                form.save()

    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form' : form
    }
    return render(request, 'users/profileupdate.html', context)


