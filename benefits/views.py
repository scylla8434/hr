from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import BenefitPlan, Enrollment, WellnessProgram, WellnessActivity, WellnessParticipation
from .forms import (
    BenefitPlanForm, EnrollmentForm, WellnessProgramForm,
    WellnessActivityForm, WellnessParticipationForm
)

@login_required
def dashboard(request):
    """Benefits dashboard view"""
    user = request.user
    enrollments = Enrollment.objects.filter(employee=user).order_by('-created_at')[:5]
    wellness_programs = WellnessProgram.objects.filter(is_active=True)
    participations = WellnessParticipation.objects.filter(employee=user).order_by('-created_at')[:5]
    
    context = {
        'enrollments': enrollments,
        'wellness_programs': wellness_programs,
        'participations': participations,
    }
    return render(request, 'benefits/dashboard.html', context)

# Benefit Plan Views
@login_required
def plan_list(request):
    """List all benefit plans"""
    plans = BenefitPlan.objects.filter(is_active=True)
    return render(request, 'benefits/plan_list.html', {'plans': plans})

@login_required
def plan_create(request):
    """Create a new benefit plan"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to create benefit plans.')
        return redirect('benefits:plan_list')
    
    if request.method == 'POST':
        form = BenefitPlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Benefit plan created successfully!')
            return redirect('benefits:plan_list')
    else:
        form = BenefitPlanForm()
    
    return render(request, 'benefits/plan_form.html', {'form': form, 'action': 'Create'})

@login_required
def plan_detail(request, pk):
    """View benefit plan details"""
    plan = get_object_or_404(BenefitPlan, pk=pk, is_active=True)
    return render(request, 'benefits/plan_detail.html', {'plan': plan})

@login_required
def plan_edit(request, pk):
    """Edit a benefit plan"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to edit benefit plans.')
        return redirect('benefits:plan_list')
    
    plan = get_object_or_404(BenefitPlan, pk=pk)
    
    if request.method == 'POST':
        form = BenefitPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Benefit plan updated successfully!')
            return redirect('benefits:plan_detail', pk=plan.pk)
    else:
        form = BenefitPlanForm(instance=plan)
    
    return render(request, 'benefits/plan_form.html', {'form': form, 'action': 'Edit'})

@login_required
def plan_delete(request, pk):
    """Delete a benefit plan"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to delete benefit plans.')
        return redirect('benefits:plan_list')
    
    plan = get_object_or_404(BenefitPlan, pk=pk)
    
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Benefit plan deleted successfully!')
        return redirect('benefits:plan_list')
    
    return render(request, 'benefits/plan_confirm_delete.html', {'plan': plan})

# Enrollment Views
@login_required
def enrollment_list(request):
    """List all enrollments"""
    enrollments = Enrollment.objects.filter(employee=request.user).order_by('-created_at')
    return render(request, 'benefits/enrollment_list.html', {'enrollments': enrollments})

@login_required
def enrollment_create(request):
    """Create a new enrollment"""
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.employee = request.user
            enrollment.save()
            messages.success(request, 'Enrollment created successfully!')
            return redirect('benefits:enrollment_list')
    else:
        form = EnrollmentForm()
    
    return render(request, 'benefits/enrollment_form.html', {'form': form, 'action': 'Create'})

@login_required
def enrollment_detail(request, pk):
    """View enrollment details"""
    enrollment = get_object_or_404(Enrollment, pk=pk, employee=request.user)
    return render(request, 'benefits/enrollment_detail.html', {'enrollment': enrollment})

@login_required
def enrollment_edit(request, pk):
    """Edit an enrollment"""
    enrollment = get_object_or_404(Enrollment, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment updated successfully!')
            return redirect('benefits:enrollment_detail', pk=enrollment.pk)
    else:
        form = EnrollmentForm(instance=enrollment)
    
    return render(request, 'benefits/enrollment_form.html', {'form': form, 'action': 'Edit'})

@login_required
def enrollment_delete(request, pk):
    """Delete an enrollment"""
    enrollment = get_object_or_404(Enrollment, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Enrollment deleted successfully!')
        return redirect('benefits:enrollment_list')
    
    return render(request, 'benefits/enrollment_confirm_delete.html', {'enrollment': enrollment})

# Wellness Program Views
@login_required
def wellness_list(request):
    """List all wellness programs"""
    programs = WellnessProgram.objects.filter(is_active=True)
    return render(request, 'benefits/wellness_list.html', {'programs': programs})

@login_required
def wellness_create(request):
    """Create a new wellness program"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to create wellness programs.')
        return redirect('benefits:wellness_list')
    
    if request.method == 'POST':
        form = WellnessProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wellness program created successfully!')
            return redirect('benefits:wellness_list')
    else:
        form = WellnessProgramForm()
    
    return render(request, 'benefits/wellness_form.html', {'form': form, 'action': 'Create'})

@login_required
def wellness_detail(request, pk):
    """View wellness program details"""
    program = get_object_or_404(WellnessProgram, pk=pk, is_active=True)
    activities = program.activities.filter(is_active=True)
    return render(request, 'benefits/wellness_detail.html', {
        'program': program,
        'activities': activities
    })

@login_required
def wellness_edit(request, pk):
    """Edit a wellness program"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to edit wellness programs.')
        return redirect('benefits:wellness_list')
    
    program = get_object_or_404(WellnessProgram, pk=pk)
    
    if request.method == 'POST':
        form = WellnessProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wellness program updated successfully!')
            return redirect('benefits:wellness_detail', pk=program.pk)
    else:
        form = WellnessProgramForm(instance=program)
    
    return render(request, 'benefits/wellness_form.html', {'form': form, 'action': 'Edit'})

@login_required
def wellness_delete(request, pk):
    """Delete a wellness program"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to delete wellness programs.')
        return redirect('benefits:wellness_list')
    
    program = get_object_or_404(WellnessProgram, pk=pk)
    
    if request.method == 'POST':
        program.delete()
        messages.success(request, 'Wellness program deleted successfully!')
        return redirect('benefits:wellness_list')
    
    return render(request, 'benefits/wellness_confirm_delete.html', {'program': program})

# Wellness Activity Views
@login_required
def activity_list(request):
    """List all wellness activities"""
    activities = WellnessActivity.objects.filter(is_active=True)
    return render(request, 'benefits/activity_list.html', {'activities': activities})

@login_required
def activity_create(request):
    """Create a new wellness activity"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to create wellness activities.')
        return redirect('benefits:activity_list')
    
    if request.method == 'POST':
        form = WellnessActivityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wellness activity created successfully!')
            return redirect('benefits:activity_list')
    else:
        form = WellnessActivityForm()
    
    return render(request, 'benefits/activity_form.html', {'form': form, 'action': 'Create'})

@login_required
def activity_detail(request, pk):
    """View wellness activity details"""
    activity = get_object_or_404(WellnessActivity, pk=pk, is_active=True)
    return render(request, 'benefits/activity_detail.html', {'activity': activity})

@login_required
def activity_edit(request, pk):
    """Edit a wellness activity"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to edit wellness activities.')
        return redirect('benefits:activity_list')
    
    activity = get_object_or_404(WellnessActivity, pk=pk)
    
    if request.method == 'POST':
        form = WellnessActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wellness activity updated successfully!')
            return redirect('benefits:activity_detail', pk=activity.pk)
    else:
        form = WellnessActivityForm(instance=activity)
    
    return render(request, 'benefits/activity_form.html', {'form': form, 'action': 'Edit'})

@login_required
def activity_delete(request, pk):
    """Delete a wellness activity"""
    if not request.user.role in ['hr', 'admin']:
        messages.error(request, 'You do not have permission to delete wellness activities.')
        return redirect('benefits:activity_list')
    
    activity = get_object_or_404(WellnessActivity, pk=pk)
    
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Wellness activity deleted successfully!')
        return redirect('benefits:activity_list')
    
    return render(request, 'benefits/activity_confirm_delete.html', {'activity': activity})

# Wellness Participation Views
@login_required
def participation_list(request):
    """List all wellness participations"""
    participations = WellnessParticipation.objects.filter(employee=request.user).order_by('-created_at')
    return render(request, 'benefits/participation_list.html', {'participations': participations})

@login_required
def participation_create(request):
    """Create a new wellness participation"""
    if request.method == 'POST':
        form = WellnessParticipationForm(request.POST)
        if form.is_valid():
            participation = form.save(commit=False)
            participation.employee = request.user
            participation.save()
            messages.success(request, 'Wellness participation created successfully!')
            return redirect('benefits:participation_list')
    else:
        form = WellnessParticipationForm()
    
    return render(request, 'benefits/participation_form.html', {'form': form, 'action': 'Create'})

@login_required
def participation_detail(request, pk):
    """View wellness participation details"""
    participation = get_object_or_404(WellnessParticipation, pk=pk, employee=request.user)
    return render(request, 'benefits/participation_detail.html', {'participation': participation})

@login_required
def participation_edit(request, pk):
    """Edit a wellness participation"""
    participation = get_object_or_404(WellnessParticipation, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        form = WellnessParticipationForm(request.POST, instance=participation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wellness participation updated successfully!')
            return redirect('benefits:participation_detail', pk=participation.pk)
    else:
        form = WellnessParticipationForm(instance=participation)
    
    return render(request, 'benefits/participation_form.html', {'form': form, 'action': 'Edit'})

@login_required
def participation_delete(request, pk):
    """Delete a wellness participation"""
    participation = get_object_or_404(WellnessParticipation, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        participation.delete()
        messages.success(request, 'Wellness participation deleted successfully!')
        return redirect('benefits:participation_list')
    
    return render(request, 'benefits/participation_confirm_delete.html', {'participation': participation})
