from django import forms

class SummyForm(forms.Form):
    text = forms.CharField(max_length=20000, widget=forms.Textarea)

class AudioForm(forms.Form):
    text = forms.CharField(max_length=20000, widget=forms.Textarea)
    isSummarized = forms.BooleanField(required=False)

class PowerPointForm(forms.Form):
    text = forms.CharField(max_length=20000, widget=forms.Textarea)

class VideoForm(forms.Form):
    text = forms.CharField(max_length=2000, widget=forms.Textarea)
    need_summarize = forms.BooleanField(required=False)
    image = forms.ImageField()
