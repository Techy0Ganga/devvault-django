from django.shortcuts import render
from django.views import generic
from .models import Presets, Stack
from .forms import presetForm, stackForm
from django.http import request
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

stackFormSet = inlineformset_factory(Presets, Stack,form=stackForm, extra=1, can_delete=False)

class ListPresets(generic.ListView):
    template_name = "generator/presets.html"
    context_object_name = "latest_preset_list"

    def get_queryset(self):
        return Presets.objects.order_by("-created_at")
    
# class AddPreset(generic.FormView):
#     template_name = "generator/addpresets.html"
#     form_class = presetForm #stackForm
#     success_url = "/preset"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

def AddPreset(request):

    if request.method == "POST":

        form = presetForm(request.POST)
        formset = stackFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            parent_obj = form.save()
            formset.instance = parent_obj
            formset.save()
            return redirect('generator:detailPreset', pk=parent_obj.pk)

        
    else:
        form = presetForm()
        formset = stackFormSet()

        context = {"form" : form, "formset" : formset}
        return render(request, 'generator/addpresets.html', context)
    
    return render(request, "generator/addpresets.html", {"form": form, "formset": formset})
    

class presetDetail(generic.DetailView):
    model = Presets
    template_name = 'generator/details.html'
    context_object_name = 'display_preset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stacks"] = Stack.objects.filter(preset=self.object)
        return context

    


