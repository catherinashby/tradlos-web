from django.db import models

class SystemMessage(models.Model):
    #   id
    message_text = models.TextField()
    message_added = models.DateTimeField(auto_now_add=True)
    message_removed = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        stamp = self.message_added.astimezone().strftime('%x,%X')
        return '{} {}'.format(stamp, self.message_text)

    class Meta:
        db_table = 'tradlos_sysmessage'

class EventMessage(models.Model):
    #   id
    event_title = models.CharField(max_length=100)
    event_body = models.TextField()
    event_added = models.DateTimeField(auto_now_add=True)
    event_removed = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        stamp = self.event_added.astimezone().strftime('%x,%X')
        return '{} {}'.format(stamp, self.event_title )

    class Meta:
        db_table = 'tradlos_eventmessage'
