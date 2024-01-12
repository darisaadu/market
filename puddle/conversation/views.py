from django.shortcuts import render, redirect, get_object_or_404
from . models import Conversation, ConversationMessage
from . forms import ConversationMessageForm
from item.models import Item


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if request.user == item.created_by:
        return redirect('dashboard:index')


    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    # if conversations:
    #     return redirect('conversation:detail', pk=conversation.first().id)

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)


    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversations = Conversation.objects.create(item=item)
            conversations.members.add(request.user)
            conversations.members.add(item.created_by)
            conversations.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversations = conversations
            conversation_message.created_by = request.user 
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    
    return render(request, "conversation/new.html", {
        'form': form
        })

def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
            'conversations': conversations
        })


def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
        
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })
    