from django.forms import ModelForm, forms

from .models import Invitation, User


class InvitationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(InvitationForm, self).__init__(*args, **kwargs)
        self.fields['to_user'].queryset = User.objects.exclude(id=user.id)

    class Meta:
        model = Invitation
        exclude = ('from_user', 'timestamp')



