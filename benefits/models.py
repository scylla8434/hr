from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class BenefitPlan(models.Model):
    """Benefit plan model"""
    TYPE_CHOICES = (
        ('health', 'Health Insurance'),
        ('dental', 'Dental Insurance'),
        ('vision', 'Vision Insurance'),
        ('life', 'Life Insurance'),
        ('retirement', 'Retirement Plan'),
        ('wellness', 'Wellness Program'),
    )
    
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    provider = models.CharField(max_length=200)
    coverage_details = models.TextField()
    monthly_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Enrollment(models.Model):
    """Employee benefit enrollment model"""
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    )
    
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    benefit_plan = models.ForeignKey(BenefitPlan, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employee_contribution = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employer_contribution = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.benefit_plan.name}"

class WellnessProgram(models.Model):
    """Wellness program model"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    points_available = models.IntegerField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class WellnessActivity(models.Model):
    """Wellness activity model"""
    program = models.ForeignKey(WellnessProgram, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(validators=[MinValueValidator(0)])
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.program.name})"

class WellnessParticipation(models.Model):
    """Employee wellness program participation model"""
    STATUS_CHOICES = (
        ('registered', 'Registered'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wellness_participations')
    activity = models.ForeignKey(WellnessActivity, on_delete=models.CASCADE, related_name='participations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')
    points_earned = models.IntegerField(default=0)
    completion_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.employee.get_full_name()} - {self.activity.name}"
