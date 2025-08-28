         income_id = kwargs.get('pk')
         new_income = get_new_type_operation(Income, income_id, request)
 
         messages.success(request, 'Расход успешно скопирован.')
         return redirect(
            reverse_lazy('income:change', kwargs={'pk': new_income.pk}),
         )
 
 