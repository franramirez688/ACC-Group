from django.db import models


class MafiaMember(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)

    # Experience
    labor_seniority = models.IntegerField(default=0, blank=True, null=True)

    # Social status
    level = models.IntegerField(default=0, blank=True, null=True)
    imprisoned = models.BooleanField(default=False)
    promoted = models.BooleanField(default=False)

    # Possible boss
    boss = models.ForeignKey('MafiaMember',
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL,  # Do nothing/Subordinates will have other boss
                             related_name="subordinates")

    def __str__(self):
        return "{name} - {city}".format(name=self.name, city=self.city)

    def save(self, *args, **kwargs):
        self.level = self.get_level()
        super().save(*args, **kwargs)

    def get_all_subordinates(self, subordinates=None):
        """Recursive"""
        all = list()
        for direct_sub in self.subordinates():
            all.append(direct_sub)
            all.extend(direct_sub.get_all_subordinates())
        return all

    def get_level(self):
        return self.subordinates().count() // 10  # improvised rule boss level

    def imprison(self):
        pass

    def release_from_prison(self):
        pass


class MafiaEventsHistory(models.Model):
    imprisoned_name = models.CharField(max_length=50, unique=True)
