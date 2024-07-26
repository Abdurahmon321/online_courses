from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile, Course, Lesson, Video, Comment, LikeVideo, DislikeVideo, Follow


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """User profiledagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('fullname', 'address', 'display_image')

    """Display image admin panelda rasmni chiqarib berish uchun"""
    def display_image(self, obj):
        return format_html('<img src="{}" width="50px" height="50px"/>',
                           obj.img.url) if obj.img else None
    display_image.short_description = 'Image'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Coursedagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('name', 'author', 'created_at', 'updated_at')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Lessondagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('title', 'author', 'course', 'created_at', 'updated_at')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Videodagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('title', 'author', 'lesson', 'upload_date', 'display_video')

    """Display video admin panelda videoni chiqarib berish uchun"""
    def display_video(self, obj):
        return format_html('<video width="320" height="240" controls><source src="{}" type="video/mp4"></video>',
                           obj.video.url) if obj.video.url else None
    display_video.short_description = 'Video'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Commentdagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('content', 'author', 'video', 'created_at')


@admin.register(LikeVideo)
class LikeVideoAdmin(admin.ModelAdmin):
    """LikeVideodagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('video', 'user', 'created_at')


@admin.register(DislikeVideo)
class DislikeVideoAdmin(admin.ModelAdmin):
    """DislikeVideodagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('video', 'user', 'created_at')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Followdagi ma'lumotlarni admin panelda chiqarish uchun"""
    list_display = ('follower', 'followed_user', 'created_at')
