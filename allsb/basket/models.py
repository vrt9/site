from django.db import models
'''
class basket(models.Model):# Create your models here.

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    timecreate = models.DateTimeField(auto_now_add=True)
'''
class Indextable(models.Model):
    #number = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=4, blank=True, null=True)
    player = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    pos = models.CharField(max_length=4, blank=True, null=True)
    min = models.CharField(max_length=26, blank=True, null=True)
    fgm_a = models.CharField(max_length=16, blank=True, null=True)
    number_3pm_a = models.CharField(db_column='3pm_a', max_length=16, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ftm_a = models.CharField(max_length=16, blank=True, null=True)
    fic = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    off = models.IntegerField(blank=True, null=True)
    def_field = models.IntegerField(db_column='def', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    reb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    too = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indextable'


class T4(models.Model):
    p3time = models.CharField(max_length=45, blank=True, null=True)
    p3status = models.CharField(max_length=45, blank=True, null=True)
    p3listvizit = models.CharField(max_length=245, blank=True, null=True)
    p3listhome25 = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't4'


class Tablegameday(models.Model):
    p3time = models.CharField(max_length=25, blank=True, null=True)
    p3teamviz = models.CharField(max_length=25, blank=True, null=True)
    p3teamhome = models.CharField(max_length=25, blank=True, null=True)
    tvizwl = models.CharField(max_length=10, blank=True, null=True)
    thomwl = models.CharField(max_length=10, blank=True, null=True)
    p3status = models.CharField(max_length=30, blank=True, null=True)
    p3listvizit = models.CharField(max_length=230, blank=True, null=True)
    p3listvizit100 = models.CharField(max_length=230, blank=True, null=True)
    p3listvizit75 = models.CharField(max_length=230, blank=True, null=True)
    p3listvizit50 = models.CharField(max_length=230, blank=True, null=True)
    p3listvizit25 = models.CharField(max_length=230, blank=True, null=True)
    p3listvizit0 = models.CharField(max_length=230, blank=True, null=True)
    p3status2 = models.CharField(max_length=30, blank=True, null=True)
    p3listhome = models.CharField(max_length=230, blank=True, null=True)
    p3listhome100 = models.CharField(max_length=230, blank=True, null=True)
    p3listhome75 = models.CharField(max_length=230, blank=True, null=True)
    p3listhome50 = models.CharField(max_length=230, blank=True, null=True)
    p3listhome25 = models.CharField(max_length=230, blank=True, null=True)
    p3listhome0 = models.CharField(max_length=230, blank=True, null=True)
    p3date = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tablegameday'


class Indextable5(models.Model):
    number = models.CharField(max_length=4, blank=True, null=True)
    player = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    pos = models.CharField(max_length=4, blank=True, null=True)
    min = models.CharField(max_length=26, blank=True, null=True)
    fgm_a = models.CharField(max_length=16, blank=True, null=True)
    number_3pm_a = models.CharField(db_column='3pm_a', max_length=16, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ftm_a = models.CharField(max_length=16, blank=True, null=True)
    fic = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    off = models.IntegerField(blank=True, null=True)
    def_field = models.IntegerField(db_column='def', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    reb = models.IntegerField(blank=True, null=True)
    ast = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    blk = models.IntegerField(blank=True, null=True)
    too = models.IntegerField(blank=True, null=True)
    pts = models.IntegerField(blank=True, null=True)
    data = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indextable5'


class Bdgameday(models.Model):
    p3time = models.CharField(max_length=15, blank=True, null=True)
    p3teamviz = models.CharField(max_length=45, blank=True, null=True)
    p3teamhome = models.CharField(max_length=45, blank=True, null=True)
    tvizwl = models.CharField(max_length=45, blank=True, null=True)
    thomwl = models.CharField(max_length=45, blank=True, null=True)
    p3status = models.CharField(max_length=45, blank=True, null=True)
    p3listvizit = models.CharField(max_length=250, blank=True, null=True)
    p3listvizit100 = models.CharField(max_length=250, blank=True, null=True)
    p3listvizit75 = models.CharField(max_length=250, blank=True, null=True)
    p3listvizit50 = models.CharField(max_length=250, blank=True, null=True)
    p3listvizit25 = models.CharField(max_length=250, blank=True, null=True)
    p3listvizit0 = models.CharField(max_length=250, blank=True, null=True)
    p3status2 = models.CharField(max_length=45, blank=True, null=True)
    p3listhome = models.CharField(max_length=250, blank=True, null=True)
    p3listhome100 = models.CharField(max_length=250, blank=True, null=True)
    p3listhome75 = models.CharField(max_length=250, blank=True, null=True)
    p3listhome50 = models.CharField(max_length=250, blank=True, null=True)
    p3listhome25 = models.CharField(max_length=250, blank=True, null=True)
    p3listhome0 = models.CharField(max_length=250, blank=True, null=True)
    p3date = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bdgameday'
