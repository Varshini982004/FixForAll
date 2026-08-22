from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Complaint
# ==============================
# HOME PAGE
# ==============================

def home(request):
    return render(
        request,
        'complaints/home.html'
    )

# ==========================================
# REPORT COMPLAINT
# ==========================================

@login_required
def report_complaint(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        issue_type = request.POST.get('issue_type')
        description = request.POST.get('description')
        location = request.POST.get('location')
        image = request.FILES.get('image')

        Complaint.objects.create(
            user=request.user,
            title=title,
            issue_type=issue_type,
            description=description,
            location=location,
            image=image
        )

        return redirect('report_success')

    return render(
        request,
        'complaints/report.html'
    )


# ==========================================
# REPORT SUCCESS
# ==========================================

@login_required
def report_success(request):

    return render(
        request,
        'complaints/success.html'
    )


# ==========================================
# MY REPORTS
# ==========================================

@login_required
def my_reports(request):

    complaints = Complaint.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'complaints/my_reports.html',
        {
            'complaints': complaints
        }
    )


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@staff_member_required
def admin_dashboard(request):

    complaints = Complaint.objects.all().order_by('-created_at')

    # Search
    search = request.GET.get('search')

    if search:
        complaints = complaints.filter(
            title__icontains=search
        ) | complaints.filter(
            location__icontains=search
        ) | complaints.filter(
            issue_type__icontains=search
        )

    # Filter by status
    status = request.GET.get('status')

    if status:
        complaints = complaints.filter(status=status)

    # Counts
    total_count = Complaint.objects.count()

    submitted_count = Complaint.objects.filter(
        status='submitted'
    ).count()

    verified_count = Complaint.objects.filter(
        status='verified'
    ).count()

    assigned_count = Complaint.objects.filter(
        status='assigned'
    ).count()

    in_progress_count = Complaint.objects.filter(
        status='in_progress'
    ).count()

    resolved_count = Complaint.objects.filter(
        status='resolved'
    ).count()

    rejected_count = Complaint.objects.filter(
        status='rejected'
    ).count()

    return render(
        request,
        'complaints/admin_dashboard.html',
        {
            'complaints': complaints,
            'status_choices': Complaint.STATUS_CHOICES,

            'total_count': total_count,
            'submitted_count': submitted_count,
            'verified_count': verified_count,
            'assigned_count': assigned_count,
            'in_progress_count': in_progress_count,
            'resolved_count': resolved_count,
            'rejected_count': rejected_count,
        }
    )


# ==========================================
# UPDATE COMPLAINT STATUS
# ==========================================

@staff_member_required
def update_complaint_status(request, complaint_id):

    complaint = get_object_or_404(
        Complaint,
        id=complaint_id
    )

    if request.method == 'POST':

        new_status = request.POST.get('status')

        # Get valid status values from model
        valid_statuses = [
            choice[0]
            for choice in Complaint.STATUS_CHOICES
        ]

        if new_status in valid_statuses:

            complaint.status = new_status
            complaint.save()

    return redirect('admin_dashboard')


# ==========================================
# ASSIGN DEPARTMENT
# ==========================================

@login_required
def assign_department(request, complaint_id):

    complaint = get_object_or_404(
        Complaint,
        id=complaint_id
    )

    if request.method == "POST":

        department = request.POST.get("department")

        complaint.department = department

        # Automatically update status
        if department:
            complaint.status = "assigned"

        complaint.save()

    return redirect("admin_dashboard")