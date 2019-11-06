from django.db import models


class ModelBase(models.Model):
    """
        This is a abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class User(ModelBase):
    """
        Custom User model
    """
    user_id = models.CharField(max_length=100, null=False)
    user_name = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100, null=False)
    channel_name = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100, null=False)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id


class Task(ModelBase):
    """
        Model to save tasks
    """
    task_name = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_users')

    def __str__(self):
        return self.task_name
