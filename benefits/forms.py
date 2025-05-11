from django import forms
from .models import BenefitPlan, Enrollment, WellnessProgram, WellnessActivity, WellnessParticipation

class BenefitPlanForm(forms.ModelForm):
    """Form for creating and editing benefit plans"""
    class Meta:
        model = BenefitPlan
        fields = ['name', 'type', 'description', 'provider', 'coverage_details', 'monthly_cost', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'provider': forms.TextInput(attrs={'class': 'form-control'}),
            'coverage_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'monthly_cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EnrollmentForm(forms.ModelForm):
    """Form for creating and editing enrollments"""
    class Meta:
        model = Enrollment
        fields = ['benefit_plan', 'status', 'start_date', 'end_date', 'coverage_amount', 'employee_contribution', 'employer_contribution']
        widgets = {
            'benefit_plan': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'coverage_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'employee_contribution': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'employer_contribution': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['benefit_plan'].queryset = BenefitPlan.objects.filter(is_active=True)

class WellnessProgramForm(forms.ModelForm):
    """Form for creating and editing wellness programs"""
    class Meta:
        model = WellnessProgram
        fields = ['name', 'description', 'start_date', 'end_date', 'points_available', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'points_available': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class WellnessActivityForm(forms.ModelForm):
    """Form for creating and editing wellness activities"""
    class Meta:
        model = WellnessActivity
        fields = ['program', 'name', 'description', 'points', 'start_date', 'end_date', 'is_active']
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'points': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program'].queryset = WellnessProgram.objects.filter(is_active=True)

class WellnessParticipationForm(forms.ModelForm):
    """Form for creating and editing wellness participations"""
    class Meta:
        model = WellnessParticipation
        fields = ['activity', 'status', 'points_earned', 'completion_date']
        widgets = {
            'activity': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'points_earned': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'completion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['activity'].queryset = WellnessActivity.objects.filter(is_active=True) 