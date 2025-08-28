     if 'role' not in session or 'username' not in session:
         return redirect(url_for('main.index'))  # Redirect to login if not authenticated
 
    # Role verification: only admin can access
    if session['role'] != 'admin' or session['username'] != username:
        return "Unauthorized Access: You must be an admin to view this page.", 403
 
     # If the method is POST, update the grades
     if request.method == 'POST':