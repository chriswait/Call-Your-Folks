from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return unicode(self.name)
    def generate_recommended_calls(self):
        for contact in self.contacts.all():
            contact.generate_recommended_call()

class Contact(models.Model):
    user = models.ForeignKey('User', related_name='contacts')
    avatar = models.ForeignKey('Avatar')
    name = models.CharField(max_length=200)
    period = models.IntegerField(null=True)
    def __unicode__(self):
        return unicode(self.name)

    def remove_current_recommended_call(self):
        for call in self.calls.filter(recommended=True):
            call.delete()

    def generate_recommended_call(self):
        self.remove_current_recommended_call()
        recent = self.calls.filter(happened=True).latest('date')
        next_call_date = recent.date + timedelta(days=self.period)
        call = Call(user=self.user, contact=self, date=next_call_date, happened=False, recommended=True)
        call.save()

class Call(models.Model):
    user = models.ForeignKey('User', related_name='calls')
    contact = models.ForeignKey('Contact', related_name='calls')
    date = models.DateField()
    happened = models.NullBooleanField(null=True)
    recommended = models.NullBooleanField(null=True)
    def __unicode__(self):
        description = "%s -> %s (%s)" % (self.user, self.contact, self.date)
        return unicode(description)

class Avatar(models.Model):
    url = models.URLField(null=True)
    def __unicode__(self):
        return unicode(self.url)
