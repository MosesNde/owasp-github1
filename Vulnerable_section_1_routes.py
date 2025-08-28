     if request.method == "POST":
         query = request.form["text"]
         if len(query) < 1:
            return render_template("error.html", error="Please enter a search term.")
         if len(query) > 50:
            return render_template("error.html", error="Please keep your search term below 50 characters.")
        sql = text("SELECT id, name, description FROM cafes WHERE LOWER(name) LIKE LOWER(:text) OR LOWER(description) LIKE LOWER(:text)")
         result = db.session.execute(sql, {"text":"%"+query+"%"})
         results = result.fetchall()
         return render_template("results.html", results=results)
 @app.route("/cafe")
 def cafe():
     cafe_id = request.args.get("id")
    result = db.session.execute(text(f"SELECT cafes.name, cafes.description, \
                                     cafes.added, cafes.updated, users.username \
                                     FROM cafes, users WHERE cafes.id={cafe_id} \
                                     AND cafes.visible=TRUE AND cafes.added_by = users.id"))
     cafe_listing = result.fetchall()
    result = db.session.execute(text(f"SELECT reviews.id, users.username, \
                                     reviews.review, reviews.added \
                                     FROM reviews, users WHERE cafe_id={cafe_id} \
                                     AND reviews.author = users.id AND visible=TRUE"))
     reviews = result.fetchall()
    result = db.session.execute(text(f"SELECT tags.id, tags.name FROM tags, tagmap, cafes WHERE tagmap.tag_id = tags.id AND tagmap.cafe_id = cafes.id AND cafes.id = {cafe_id}"))
     tag_list = result.fetchall()
    return render_template("cafe.html", cafe=cafe_listing, reviews=reviews, id=cafe_id, tags=tag_list)
 
 @app.route("/tag")
 def tag():
     tag_id = request.args.get("id")
    result = db.session.execute(text(f"SELECT tags.id, tags.name FROM tags WHERE tags.id={tag_id} AND tags.visible=TRUE"))
     tag_listing = result.fetchall()
    result = db.session.execute(text(f"SELECT cafes.id, cafes.name, cafes.description FROM tags, tagmap, cafes WHERE tagmap.tag_id = tags.id AND tags.id = {tag_id} AND tagmap.cafe_id = cafes.id AND tags.visible = TRUE AND cafes.visible = TRUE"))
     cafes = result.fetchall()
     return render_template("tag.html", cafes=cafes, id=tag_id, tag=tag_listing)
 
                                error="Sorry, please keep your description below 5000 characters.")
     sql = text("INSERT INTO cafes (name, description, visible, added, updated, added_by) \
                VALUES (:name, :description, TRUE, NOW(), NOW(), :user) RETURNING id")
    result = db.session.execute(sql, {"name":name, "description":description, "user":users.user_id()})
     db.session.commit()
     cafe_id = result.fetchone()[0]
     for tag_id in request.form.getlist("tags"):