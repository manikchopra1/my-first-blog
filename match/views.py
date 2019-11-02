from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProposeForm
from users.models import Profile
from .models import Propose

@login_required
def home(request):

    user = request.user
    profile = Profile.objects.filter(id = user.id)
    proposals = Propose.objects.filter(user = request.user).count()
    context = {
        'user': user,
        'profile' : profile,
        'proposals' : proposals,
    }
    return render(request, 'match/home.html', context)

def view_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    age = profile.age()
    context = {
        'profile' : profile,
        'age' : age,
    }
    return render(request, 'match/profile.html', context)


def propose(request, pk):

    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':

        form = ProposeForm(request.POST)
        if form.is_valid():

            user = request.user
            proposal = Propose.objects.create(user = request.user, to_user = profile.user)
            proposal.message = form.cleaned_data['message']
            user.profile.proposals.add(proposal)
            user.profile.save()
            profile.save()
            proposal.save()

            return redirect('home')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'match/propose.html', context)


@login_required
def proposal_home(request, pk):
    proposal = get_object_or_404(Propose, pk=pk)
    context = {
        'proposal' : proposal
    }
    return render(request, 'match/proposal_home.html', context)


@login_required
def accept_proposal(request, pk):

    proposal = get_object_or_404(Proposal, pk=pk)

    proposal.user.profile.relationshipstatus = 'committed'
    proposal.to_user.profile.relationshipstatus = 'committed'
    proposal.relationshipstatus = 'committed'

    proposal.user.profile.save()
    proposal.to_user.profile.save()
    proposal.save()
    return render(request, 'matching/profile.html')

@login_required
def decline_proposal(request, pk):

    proposal = get_object_or_404(Propose, pk=pk)
    proposal.relationshipstatus = 'single'
    proposal.save()
    return render(request, 'matching/profile.html')


