from django.contrib import admin
from .models import user, mathematics, mathematics2, english, english2, bscience, bscience2, btech, btech2, agric, agric2, bstd, bstd2, yoruba, yoruba2, cca, cca2, hecons, hecons2, phe, phe2, it, it2, civic, civic2, sstd, sstd2, crk, crk2
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display =("username", "age","gender", "scorecrs", "scoreagric")

class mathematicsAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class mathematics2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class englishAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class english2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class bscienceAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class bscience2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class btechAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class btech2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class agricAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class agric2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class bstdAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class bstd2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class yorubaAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class yoruba2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class ccaAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class cca2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class heconsAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class hecons2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class pheAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class phe2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class itAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class it2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class civicAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class civic2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class sstdAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class sstd2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")

class crkAdmin(admin.ModelAdmin):
    list_display = ("no", "quest", "a", "b", "c", "d", "correct")
class crk2Admin(admin.ModelAdmin):
    list_display = ("no", "quest")


admin.site.register(user, userAdmin)
admin.site.register(mathematics, mathematicsAdmin)
admin.site.register(mathematics2, mathematics2Admin)

admin.site.register(english, englishAdmin)
admin.site.register(english2, english2Admin)

admin.site.register(bscience, bscienceAdmin)
admin.site.register(bscience2, bscience2Admin)

admin.site.register(btech, btechAdmin)
admin.site.register(btech2, btech2Admin)

admin.site.register(agric, agricAdmin)
admin.site.register(agric2, agric2Admin)

admin.site.register(bstd, bstdAdmin)
admin.site.register(bstd2, bstd2Admin)

admin.site.register(yoruba, yorubaAdmin)
admin.site.register(yoruba2, yoruba2Admin)

admin.site.register(cca, ccaAdmin)
admin.site.register(cca2, cca2Admin)

admin.site.register(hecons, heconsAdmin)
admin.site.register(hecons2, hecons2Admin)

admin.site.register(phe, pheAdmin)
admin.site.register(phe2, phe2Admin)

admin.site.register(it, itAdmin)
admin.site.register(it2, it2Admin)

admin.site.register(civic, civicAdmin)
admin.site.register(civic2, civic2Admin)

admin.site.register(sstd, sstdAdmin)
admin.site.register(sstd2, sstd2Admin)

admin.site.register(crk, crkAdmin)
admin.site.register(crk2, crk2Admin)
