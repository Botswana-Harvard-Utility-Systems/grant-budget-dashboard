from django.views.generic import TemplateView


# from grant_budget

class StaffingBudgetView(TemplateView):
    template_name = 'grant_budget_dashboard/staffing_budget.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_budgets'] = None
