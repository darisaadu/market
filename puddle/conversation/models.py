from django.db import models
from item.models import Item
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# User = get_user_model()


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name="conversation", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversation")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="conversation_message", on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-created_at',)