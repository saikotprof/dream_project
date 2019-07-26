from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	username = cleaned_data.get('username')
    	return f'Your account has been created by name as {username} & now you are able to login'

@login_required
def profile(request):
	return render(request, 'users/profile.html')

#  from django.shortcuts import render, redirect
#    if request.method == 'POST':
#     form = UserRegisterForm(request.POST)
#    if form.is_valid():
#       form.save()
#      username = form.cleaned_data.get('username')
#     messages.success(request, f'Account created for {username}!')
#    return redirect('blog-home')
# else:
#   form = UserRegisterForm()
# return render(request, 'users/register.html', {'form': form})

