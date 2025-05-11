from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Goal, PerformanceReview, Feedback
from .forms import GoalForm, PerformanceReviewForm, FeedbackForm

@login_required
def dashboard(request):
    """Performance dashboard view"""
    user = request.user
    goals = Goal.objects.filter(employee=user).order_by('-created_at')[:5]
    reviews = PerformanceReview.objects.filter(employee=user).order_by('-created_at')[:5]
    feedback = Feedback.objects.filter(employee=user).order_by('-created_at')[:5]
    
    context = {
        'goals': goals,
        'reviews': reviews,
        'feedback': feedback,
    }
    return render(request, 'performance/dashboard.html', context)

# Goal Views
@login_required
def goal_list(request):
    """List all goals"""
    goals = Goal.objects.filter(employee=request.user).order_by('-created_at')
    return render(request, 'performance/goal_list.html', {'goals': goals})

@login_required
def goal_create(request):
    """Create a new goal"""
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.employee = request.user
            goal.save()
            messages.success(request, 'Goal created successfully!')
            return redirect('performance:goal_list')
    else:
        form = GoalForm()
    
    return render(request, 'performance/goal_form.html', {'form': form, 'action': 'Create'})

@login_required
def goal_detail(request, pk):
    """View goal details"""
    goal = get_object_or_404(Goal, pk=pk, employee=request.user)
    return render(request, 'performance/goal_detail.html', {'goal': goal})

@login_required
def goal_edit(request, pk):
    """Edit a goal"""
    goal = get_object_or_404(Goal, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goal updated successfully!')
            return redirect('performance:goal_detail', pk=goal.pk)
    else:
        form = GoalForm(instance=goal)
    
    return render(request, 'performance/goal_form.html', {'form': form, 'action': 'Edit'})

@login_required
def goal_delete(request, pk):
    """Delete a goal"""
    goal = get_object_or_404(Goal, pk=pk, employee=request.user)
    
    if request.method == 'POST':
        goal.delete()
        messages.success(request, 'Goal deleted successfully!')
        return redirect('performance:goal_list')
    
    return render(request, 'performance/goal_confirm_delete.html', {'goal': goal})

# Performance Review Views
@login_required
def review_list(request):
    """List all performance reviews"""
    reviews = PerformanceReview.objects.filter(
        Q(employee=request.user) | Q(reviewer=request.user)
    ).order_by('-created_at')
    return render(request, 'performance/review_list.html', {'reviews': reviews})

@login_required
def review_create(request):
    """Create a new performance review"""
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Performance review created successfully!')
            return redirect('performance:review_list')
    else:
        form = PerformanceReviewForm()
    
    return render(request, 'performance/review_form.html', {'form': form, 'action': 'Create'})

@login_required
def review_detail(request, pk):
    """View performance review details"""
    review = get_object_or_404(PerformanceReview, pk=pk)
    if review.employee != request.user and review.reviewer != request.user:
        messages.error(request, 'You do not have permission to view this review.')
        return redirect('performance:review_list')
    
    return render(request, 'performance/review_detail.html', {'review': review})

@login_required
def review_edit(request, pk):
    """Edit a performance review"""
    review = get_object_or_404(PerformanceReview, pk=pk, reviewer=request.user)
    
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance review updated successfully!')
            return redirect('performance:review_detail', pk=review.pk)
    else:
        form = PerformanceReviewForm(instance=review)
    
    return render(request, 'performance/review_form.html', {'form': form, 'action': 'Edit'})

@login_required
def review_delete(request, pk):
    """Delete a performance review"""
    review = get_object_or_404(PerformanceReview, pk=pk, reviewer=request.user)
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Performance review deleted successfully!')
        return redirect('performance:review_list')
    
    return render(request, 'performance/review_confirm_delete.html', {'review': review})

# Feedback Views
@login_required
def feedback_list(request):
    """List all feedback"""
    feedback = Feedback.objects.filter(
        Q(employee=request.user) | Q(reviewer=request.user)
    ).order_by('-created_at')
    return render(request, 'performance/feedback_list.html', {'feedback': feedback})

@login_required
def feedback_create(request):
    """Create new feedback"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.reviewer = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('performance:feedback_list')
    else:
        form = FeedbackForm()
    
    return render(request, 'performance/feedback_form.html', {'form': form, 'action': 'Create'})

@login_required
def feedback_detail(request, pk):
    """View feedback details"""
    feedback = get_object_or_404(Feedback, pk=pk)
    if feedback.employee != request.user and feedback.reviewer != request.user:
        messages.error(request, 'You do not have permission to view this feedback.')
        return redirect('performance:feedback_list')
    
    return render(request, 'performance/feedback_detail.html', {'feedback': feedback})

@login_required
def feedback_edit(request, pk):
    """Edit feedback"""
    feedback = get_object_or_404(Feedback, pk=pk, reviewer=request.user)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback updated successfully!')
            return redirect('performance:feedback_detail', pk=feedback.pk)
    else:
        form = FeedbackForm(instance=feedback)
    
    return render(request, 'performance/feedback_form.html', {'form': form, 'action': 'Edit'})

@login_required
def feedback_delete(request, pk):
    """Delete feedback"""
    feedback = get_object_or_404(Feedback, pk=pk, reviewer=request.user)
    
    if request.method == 'POST':
        feedback.delete()
        messages.success(request, 'Feedback deleted successfully!')
        return redirect('performance:feedback_list')
    
    return render(request, 'performance/feedback_confirm_delete.html', {'feedback': feedback})
