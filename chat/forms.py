from django import forms

class AddFriendForm(forms.Form):
    friendName = forms.CharField(max_length=30, widget=forms.TextInput(attrs= {
        'placeholder' : 'Your Friend Name'
    }))