from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
                    view_profile, home, accept_proposal, propose, proposal_home, decline_proposal,
)


urlpatterns = [
    path('', home, name='home'),
    path('user_profile/<int:pk>/', view_profile, name='view_profile'),
    path('proposal/<int:pk>/', proposal_home, name='proposal_home'),
    path('proposal/<int:pk>/accepted', accept_proposal, name='accept_proposal'),
    path('proposal/<int:pk>/declined', decline_proposal, name='decline_proposal'),
    path('profile/<int:pk>/propose/', propose, name='propose'),
]
