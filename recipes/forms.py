from django import forms


CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFIC__CHOICES = (
    ('#1', 'Easy'),
    ('#2', 'Medium'),
    ('#3', 'Intermediate'),
    ('#4', 'Hard')
)


class RecipesSearchForm(forms.Form):
    recipe_diff = forms.ChoiceField(
        label='Recipe Difficulty',
        choices=DIFFIC__CHOICES,
        required=True,
        initial='#1'

    )
    chart_type = forms.ChoiceField(
        label='Chart Type',
        choices=CHART__CHOICES,
        required=True,
        initial='#1'
    )