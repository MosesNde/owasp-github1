     queryset = JobApplication.objects.is_active_company_member(request.user)
     # Check GEIQ eligibility during job application process
     job_application = get_object_or_404(queryset, pk=job_application_id)
    back_url = request.GET.get("back_url") or reverse(
        "apply:details_for_company", kwargs={"job_application_id": job_application.pk}
     )
    next_url = request.GET.get("next_url")
     return common_views._geiq_eligibility(
         request,
         job_application.to_company,