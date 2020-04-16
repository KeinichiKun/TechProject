from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from django.views.generic import View

from .render import Render

from .models import Worker, Position, Tabel_time



# Create your views here.
def workers(request):
    worker = Worker.objects.all()
    return render(request, 'workers.html', {'worker': worker})

# добавление данных в бд
def create(request):
    pos = Position.objects.all()
    if request.method == "POST":
        tom = Worker()
        pos = Position()
        pos.id = request.POST.get("position")
        tom.first_name = request.POST.get("first_name")
        tom.middle_name = request.POST.get("middle_name")
        tom.last_name = request.POST.get("last_name")
        tom.phone = request.POST.get("phone")
        tom.passport_seria = request.POST.get("passport_seria")
        tom.passport_number = request.POST.get("passport_number")
        tom.passport_issued = request.POST.get("passport_issued")
        tom.passport_date = request.POST.get("passport_date")
        tom.adress = request.POST.get("adress")
        tom.P_position = pos
        tom.save()
        return HttpResponseRedirect("/workers")
    else:
        return render(request, "create_worker.html", {"position": pos})


# изменение данных в бд
def edit(request, id):
    try:
        pos = Position.objects.all()
        tom = Worker.objects.get(id=id)
        if request.method == "POST":
            pos = Position(id=id)
            pos.id = request.POST.get("position")
            tom.first_name = request.POST.get("first_name")
            tom.middle_name = request.POST.get("middle_name")
            tom.last_name = request.POST.get("last_name")
            tom.phone = request.POST.get("phone")
            tom.passport = request.POST.get("passport")
            tom.adress = request.POST.get("adress")
            tom.P_position = pos
            tom.save()
            return HttpResponseRedirect("/workers")
        else:
               return render(request, "edit_worker.html", {"worker": tom, 'position': pos})
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>customer не найден</h2>")

def tabel(request, id):
    try:
        tab = Tabel_time.objects.get(worker_id=id)
        if request.method == "POST":
            tab.worker = id
            tab.day1 = request.POST.get("day1")
            tab.day2 = request.POST.get("day2")
            tab.day3 = request.POST.get("day3")
            tab.day4 = request.POST.get("day4")
            tab.day5 = request.POST.get("day5")
            tab.day6 = request.POST.get("day6")
            tab.day7 = request.POST.get("day7")
            tab.day8 = request.POST.get("day8")
            tab.day9 = request.POST.get("day9")
            tab.day10 = request.POST.get("day10")
            tab.day11 = request.POST.get("day11")
            tab.day12 = request.POST.get("day12")
            tab.day13 = request.POST.get("day13")
            tab.day14 = request.POST.get("day14")
            tab.day15 = request.POST.get("day15")
            tab.day16 = request.POST.get("day16")
            tab.day17 = request.POST.get("day17")
            tab.day18 = request.POST.get("day18")
            tab.day19 = request.POST.get("day19")
            tab.day20 = request.POST.get("day20")
            tab.day21 = request.POST.get("day21")
            tab.day22 = request.POST.get("day22")
            tab.day23 = request.POST.get("day23")
            tab.day24 = request.POST.get("day24")
            tab.day25 = request.POST.get("day25")
            tab.day26 = request.POST.get("day26")
            tab.day27 = request.POST.get("day27")
            tab.day28 = request.POST.get("day28")
            tab.day29 = request.POST.get("day29")
            tab.day30 = request.POST.get("day30")
            tab.day31 = request.POST.get("day31")
            tab.save()
            return HttpResponseRedirect("/workers")
        else:
            return render(request, 'table_time.html', {'tab': tab})
    except Tabel_time.DoesNotExist:
        if request.method == "POST":
            tabel.worker = id

            tabel.save()
            return HttpResponseRedirect("/workers")
        else:
            return render(request, "table_time.html", {"tabel": tabel})

# удаление данных из бд
def delete(request, id):
    try:
        person = Worker.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/workers")
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


class Serch(ListView):
    # поиск
    model = Worker
    template_name = 'workers.html'
    def get_queryset(self):
        return Worker.objects.filter(middle_name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get("q")
        return context


#
#
#
# class Pdf(View):
#
#     def get(self, request):
#         worker = Worker.objects.all()
#        # today = timezone.now()
#         params = {
#         #    'today': today,
#             'worker': worker,
#             'request': request
#         }
#         return Render.render('pdf.html', params)