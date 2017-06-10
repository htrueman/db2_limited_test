from django import forms


class ChooseSortForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=(
            ('country', 'Country'),
            ('city', 'City'),
            ('date_of_birth', 'Date of birth'),))


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=25)
