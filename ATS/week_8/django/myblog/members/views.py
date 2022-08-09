from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserUpdateForm,ProfileUpdateForm


class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "registration/profile.html", context)