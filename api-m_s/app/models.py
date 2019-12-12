from django.db import models

# Create your models here.

class User(models.Model):
    '''
    '''
    name = models.CharField(max_length=200)

    def __str__(self):
        '''
        '''
        return self.name
    
class Task(models.Model):
    '''
    '''
    STATE = [
        (True, "Done."),
        (False, "To Do.")
    ]
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=8, choices=STATE, default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')

    def __str__(self):
        '''
        '''
        return self.description
