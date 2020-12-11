from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CommonFieldsMixin(models.Model):
    STATUS = [(0, 'Live'), (1, 'Block'), (2, 'Soft Delete'), (3, 'Permanent Delete')]
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=STATUS)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sort_order = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Permission(CommonFieldsMixin):
    USER_TYPES = [(0, 'User'), (1, 'Admin')]
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_perm')
    user_type = models.IntegerField(default=0, choices=USER_TYPES)


class Blog(CommonFieldsMixin):
    title = models.CharField(max_length=1024)


class Content(CommonFieldsMixin):
    fk_blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    content = models.CharField(max_length=2048)


class Media(CommonFieldsMixin):
    image = models.ImageField(upload_to='%H/%M/%S')
    fk_blog = models.ForeignKey('Blog', on_delete=models.CASCADE)


class Comment(CommonFieldsMixin):
    comment = models.CharField(max_length=2048)
    commenter = models.CharField(max_length=512)
