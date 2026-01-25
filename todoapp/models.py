from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    priority = models.IntegerField(default=1)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(defualt=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
def _str_(self):
    return self.title
