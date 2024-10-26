from django.contrib import admin
from .models import User, Frame, Prediction, Feedback, TrainingTask
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'created_at')


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('frame_id', 'user', 'upload_time', 'image_path')


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        'prediction_id',
        'frame',
        'predicted_class',
        'confidence',
        'timestamp')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'user', 'comment', 'timestamp')


@admin.register(TrainingTask)
class TrainingTaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'user', 'start_time', 'status', 'progress')
