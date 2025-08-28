 
         if amount > balance:
             
            # raise forms.ValidationError(
            #     f'You have {balance} $ in your account. '
            #     'You can not withdraw more than your account balance'
            # )
            try:
                raise ValueError("Attempt to withdraw more than balance")
            except ValueError as e:
                # catch error
                stack_trace = traceback.format_exc()
                error_msg = f'Insufficient funds. Your balance is ${balance}.'
                error_msg += f' Error occurred at: {stack_trace}'
                raise forms.ValidationError(error_msg)
 
         return amount
 