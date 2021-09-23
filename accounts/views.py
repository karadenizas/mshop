from django.shortcuts import render
from .forms import UserRegistrartionForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrartionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', 
                                            {'new_user': new_user})
    else:
        user_form = UserRegistrartionForm()
    return render(request, 'account/register.html', 
                            {'user_form': user_form})


def profile(request):
    return render(request, 'account/profile.html')