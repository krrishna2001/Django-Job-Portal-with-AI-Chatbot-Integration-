from django import template
from .models import Applicant

register = template.Library()

@register.filter
def get_total_applicant(jobs):
    total_applicants = 0
    for job in jobs:
        total_applicants += job.applicant_set.count()
    return total_applicants

@register.filter
def get_total_applicant_for_job(job):
    return job.applicant_set.count()