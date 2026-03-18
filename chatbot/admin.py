from django.contrib import admin
from .models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['user_message', 'intent', 'confidence', 'created_at']
    list_filter = ['intent', 'created_at']
    search_fields = ['user_message', 'bot_response']
    readonly_fields = ['created_at']
