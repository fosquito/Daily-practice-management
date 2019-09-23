from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from Users.models import User
from Activities.models import Sentence, Group, Pattern, Verb
from django.db.models import Q
from django.views.generic import ListView, TemplateView

import datetime

# Create your views here.


@login_required
def Home(request):
    return render(request,'main/home.html',
    context={"permissions":Permission.objects.values('name').filter(group__user=request.user).distinct(),
    "users":User.objects.all(),
    "sentences":Sentence.objects.all().filter(userid=request.user),
    "verbs":Verb.objects.all(),
    "groups":Group.objects.all().filter(userid=request.user),
    "patterns":Pattern.objects.all().filter(userid=request.user)})

class SearchView(TemplateView):
    template_name = 'search_form.html'


class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return query

    def get_context_data(self, **kwargs):
        # General Queries
        query_name = self.request.GET.get('name')
        query_date_initial = self.request.GET.get('date_initial')
        query_date_final = self.request.GET.get('date_final')

        # Sentence Queries
        query_frase_verbo = self.request.GET.get('frase_verbo')
        query_frase_sujeito = self.request.GET.get('frase_sujeito')
        query_frase_receptor = self.request.GET.get('frase_receptor')

        # Verb Queries
        query_verbo_tipo = self.request.GET.get('verbo_tipo')

        # Group Queries
        query_group_frases = self.request.GET.get('group_frases')

        # Pattern Queries
        query_pattern_group = self.request.GET.get('pattern_groups')

        context = super(SearchResultsView, self).get_context_data(**kwargs)

        if not query_date_initial:
            query_date_initial = datetime.date(2019, 1, 1)

        if not query_date_final:
            query_date_final = datetime.datetime.now()

        context.update({
            'sentences': Sentence.objects.all().filter(
                Q(sentencename__icontains=query_name) &
                Q(datecreated__range=[query_date_initial, query_date_final]) &
                Q(verbid__verbname__icontains=query_frase_verbo) &
                Q(subject__icontains=query_frase_sujeito) &
                Q(receiver__icontains=query_frase_receptor)
            ).distinct(),
            'verbs': Verb.objects.all().filter(
                Q(verbname__icontains=query_name) &
                Q(verbtype__icontains=query_verbo_tipo)
            ).distinct(),
            'groups': Group.objects.all().filter(
                Q(groupname__icontains=query_name) &
                Q(creationdate__range=[query_date_initial, query_date_final]) &
                Q(sentences__sentencename__icontains=query_group_frases)
            ).distinct(),
            'patterns': Pattern.objects.all().filter(
                Q(patternname__icontains=query_name) &
                Q(data_creation__range=[query_date_initial, query_date_final]) &
                Q(groups__groupname__icontains=query_pattern_group)
            ).distinct(),
        })
        return context
