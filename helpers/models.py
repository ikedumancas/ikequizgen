from django.db import models
from django.db.models import F


class SortableModel(models.Model):
    """ 
    Abstract model which makes an inherited model's records sortable
    by calling instance.move(position)
    """
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        """ 
        makes sure we have a value for order. This must be connected to the
        pre_save event for the inheriting model.
        """
        if not instance.order or instance.order == 0:
            #get last order
            try:
                last = sender.objects.values('order').order_by('-order')[0]
                instance.order = last['order'] + 1 
            except IndexError:
                instance.order = 1 
     

    def move(self, to, **kwargs):
    	model = self.__class__
        to = int(to)
        orig = self.order
        if to == orig:
            return
     
        # make sure initial ordering is "clean". Not ideal, but sometimes needed
        if kwargs:
        	queryset = model.objects.filter(**kwargs)
        else:
        	queryset = model.objects.all()
        for i, f in enumerate(queryset):
            f.order = i+1 
            f.save()

        # make some room
        shift, range = to < orig and (1, (to, orig-1)) or (-1, (orig+1, to))
        queryset.filter(order__range=range).update(order=F('order')+shift)
     
        # move it
        self.order = to
        self.save()