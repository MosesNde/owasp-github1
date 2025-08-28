         abort(403)
     review = request.form["review"]
     author = request.form["author"]
    cafe_id = request.form["cafe_id"]
     if len(review) > 2000:
         return render_template("error.html", \
                                error="Sorry, please keep your review below 2000 characters.")
                VALUES (:cafe_id, :author, :review, TRUE, NOW())")
     db.session.execute(sql, {"cafe_id":cafe_id, "author":author, "review":review})
     db.session.commit()
    return redirect(f"/cafe?id={cafe_id}")
 
 @app.route("/sendtag", methods=["POST"])
 def sendtag():