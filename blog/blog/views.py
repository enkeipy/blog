from posts.models import Post
from django.views.generic.base import TemplateView
from . forms import ContactForm

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.first()
        return context

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['kukshynsky@gmail.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
            form = ContactForm()
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})