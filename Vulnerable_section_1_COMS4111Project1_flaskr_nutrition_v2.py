 from flask import Blueprint, render_template, request, redirect, url_for, flash
 from .db import get_db
 from psycopg2.extras import DictCursor
 
 bp = Blueprint('nutrition', __name__, url_prefix='/nutrition')
 
         member_name = request.form['member_name']
 
         db = get_db()
        with db.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("SELECT member_id FROM Member WHERE name = %s", (member_name,))
            member = cursor.fetchone()
            
            if member is None:
                flash('Error: Member name does not exist in the directory. Please enter a valid member name.', 'error')
                return redirect(url_for('nutrition.add_nutrition'))

            member_id = member['member_id']
                 
            cursor.execute("""
                INSERT INTO Nutrition (name, calories, proteins, carbohydrates)
                VALUES (%s, %s, %s, %s) RETURNING nutrition_id
            """, (name, calories, proteins, carbohydrates))
            nutrition_id = cursor.fetchone()['nutrition_id']
 
            cursor.execute("INSERT INTO Tracks (member_id, nutrition_id) VALUES (%s, %s)", (member_id, nutrition_id))
            
            db.commit()
 
        flash('Successfully added to nutrition log.', 'success')
         return redirect(url_for('nutrition.index'))
 
     return render_template('nutrition/add.html')