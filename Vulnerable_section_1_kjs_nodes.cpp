       // eval-injected symbols can be deleted...
       flags &= ~DontDelete;
 
       // fallthrough intentional
     case GlobalCode:
       exec->variableObject()->put(exec, ident, makeFunctionObject(exec), flags);