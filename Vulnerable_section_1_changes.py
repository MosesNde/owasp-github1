                 text,
                 sublime.LAYOUT_INLINE,
                 wrapper_class="find-cursor",
                css=CSS
             )
         else:
             view.run_command('insert', {"characters": text})