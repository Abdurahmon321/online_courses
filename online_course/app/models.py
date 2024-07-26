from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Bu model userning profile qismi uchun"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='user_profile/', null=True, blank=True)
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.fullname


class Course(models.Model):
    """Bu model course uchun """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Bu model lessonlar uchun """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    """BU model lessonlarning videolarini saqlash uchun"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='course_video/',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Bu model videolarhga izoh"""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.video}'


class LikeVideo(models.Model):
    """Bu model videoga like qoldirish uchun"""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')

    def __str__(self):
        return f'Like by {self.user} on {self.video}'


class DislikeVideo(models.Model):
    """Bu model videoga dislike qoldirish uchun"""
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')

    def __str__(self):
        return f'Dislike by {self.user} on {self.video}'


class Follow(models.Model):
    """Bu biror bir foydalnuvchiga follow bosish uchun"""
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followed_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed_user')

    def __str__(self):
        return f'{self.follower} follows {self.followed_user}'