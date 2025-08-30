from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, "Mensaje enviado correctamente.")
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send_message.html', {'form': form})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user).order_by('-created_at')
    return render(request, 'messenger/inbox.html', {'messages': received_messages})

@login_required
def sent_messages(request):
    sent = Message.objects.filter(sender=request.user).order_by('-created_at')
    return render(request, 'messenger/sent_messages.html', {'messages': sent})
