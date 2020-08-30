from django.db import models

class user(models.Model):
    """docstring for user."""
    username = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    scorecrs = models.IntegerField()
    scoreagric = models.IntegerField()

class mathematics(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class mathematics2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class english(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class english2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class bscience(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class bscience2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class btech(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class btech2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class agric(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class agric2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class bstd(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class bstd2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class yoruba(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class yoruba2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class cca(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class cca2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class hecons(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class hecons2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class phe(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class phe2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class it(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class it2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class civic(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class civic2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class sstd(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class sstd2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"

class crk(models.Model):
    no = models.IntegerField()
    quest = models.CharField(max_length=600)
    a = models.CharField(max_length=64)
    b = models.CharField(max_length=64)
    c = models.CharField(max_length=64)
    d = models.CharField(max_length=64)
    correct = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.no}-> {self.quest} (a->{self.a}) (b->{self.b}) (c->{self.c}) (d->{self.d}) (correct->{self.correct})"

class crk2(models.Model):
    no = models.CharField(max_length=3)
    quest = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.no}-> {self.quest}"
