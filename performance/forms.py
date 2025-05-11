from django import forms
from .models import Goal, PerformanceReview, Feedback

class GoalForm(forms.ModelForm):
    """Form for creating and editing goals"""
    class Meta:
        model = Goal
        fields = ['title', 'description', 'start_date', 'end_date', 'status', 'progress']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }

class PerformanceReviewForm(forms.ModelForm):
    """Form for creating and editing performance reviews"""
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_period', 'status', 'overall_rating', 'comments']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'review_period': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'overall_rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter employees based on user's role
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['employee'].queryset = self.fields['employee'].queryset.filter(
                department=kwargs['instance'].reviewer.department
            )
        else:
            self.fields['employee'].queryset = self.fields['employee'].queryset.none()

class FeedbackForm(forms.ModelForm):
    """Form for creating and editing feedback"""
    class Meta:
        model = Feedback
        fields = ['employee', 'feedback_type', 'content', 'rating']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'feedback_type': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter employees based on user's role
        if 'instance' in kwargs and kwargs['instance']:
            self.fields['employee'].queryset = self.fields['employee'].queryset.filter(
                department=kwargs['instance'].reviewer.department
            )
        else:
            self.fields['employee'].queryset = self.fields['employee'].queryset.none() 