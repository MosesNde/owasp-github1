         msg["To"] = MY_EMAIL                                                 # 받는 사람(나)의 이메일
         msg["Subject"] = "Message from portfolio website\n\n"                # 이메일 제목 설정
         email_body = (f"Name: {data['name']}\n"                              # 이메일 본문
                      f"Email: {data['emai']}\n"
                       f"Message:\n{data['message']}")
         msg.attach(MIMEText(email_body, 'plain', 'utf-8'))  # 본문에 한글 인코딩 추가
 
         return render_template("contact.html", msg_sent=True)
 
     # 양식을 입력하고 이메일을 전송한 후에는 POST 요청
    return render_template("contact.html", msg_sent=False)
 
 
 # sample pages --------------------------------------
         return redirect(url_for('morse_code_converter', result=result, user_input=user_input))
 
     user_input = request.args.get('user_input')     # 리다이렉션된 URL의 user_input 매개변수 가져오기
    return render_template("project_morse_code.html", result=result, user_input=user_input)
 
 ###############################################################################################################
 @app.route("/laptop_friendly_cafes", defaults={'selected_city': 'Seoul'}, methods=["GET", "POST"])  # 기본 도시 값 Seoul
         db.session.add(new_cafe)
         db.session.commit()
         return redirect(url_for('laptop_friendly_cafes_home', city=new_cafe.city))
    return render_template("project_laptop_friendly_cafes_add.html")
 
 
 @app.route('/laptop_friendly_cafes/show/<int:cafe_id>', methods=["GET", "POST"])
         # 리디렉션 시 edit 파라미터 제거
         return redirect(url_for("laptop_friendly_cafes_show", cafe_id=cafe_id))
     # edit_id를 템플릿에 넘겨줌
    return render_template("project_laptop_friendly_cafes_show.html", cafe=cafe, edit_id=edit_id)
 
 
 @app.route('/laptop_friendly_cafes/delete_comment/<int:comment_id>', methods=["POST"])
         db.session.commit()
         return redirect(url_for('laptop_friendly_cafes_show', cafe_id=cafe.id))
     # GET 요청 시 수정 폼 보여주기
    return render_template("project_laptop_friendly_cafes_edit.html", cafe=cafe)
 
 
 @app.route("/laptop_friendly_cafes/delete_cafe/<int:cafe_id>", methods=["POST"])