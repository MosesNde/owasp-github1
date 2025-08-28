 
 @notes_bp.route("/search")
 def search_notes():
    """Search notes with intentional SQL injection vulnerability"""
     if "user" not in session:
         return jsonify({"success": False, "error": "Not logged in"}), 401
 
     print(f"Search query: {query}")
 
     try:
        sql = f"SELECT * FROM notes WHERE title LIKE '%{query}%' OR content LIKE '%{query}%'"

        # Log the raw SQL for debugging
        print(f"Executing SQL: {sql}")

        # Execute the raw SQL
        result = db.session.execute(text(sql))
 
         notes = []
         for row in result: