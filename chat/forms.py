from django import forms

class AddFriendForm(forms.Form):
    friendName = forms.CharField(max_length=30, widget=forms.TextInput(attrs= {
        'placeholder' : 'Your Friend Name',
        'class' : 'inputW'
    }))

    def __init__(self, *args, **kwargs):
        super(AddFriendForm, self).__init__(*args, **kwargs)
        self.fields['friendName'].label = "Friend Name"
