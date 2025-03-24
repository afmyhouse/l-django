from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # return redirect('login') ,<-- it goes directly to login form
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)  
    context = {
        'uu_form': uu_form,
        'pu_form': pu_form
    }
    return render(request, 'users/profile.html', context)
