         expense_id = kwargs.get('pk')
         new_expense = get_new_type_operation(Expense, expense_id, request)
 
         messages.success(request, 'Расход успешно скопирован.')
         return redirect(
            reverse_lazy('expense:change', kwargs={'pk': new_expense.pk}),
         )
 
 