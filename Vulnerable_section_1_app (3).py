         if user and check_password_hash(user['password'], password):
             session.clear()  # 세션 고정 공격 방지
             session['user_id'] = user['id']
             flash('로그인 성공!')
             return redirect(url_for('dashboard'))
         else:
     payload = {
         "message_id": str(uuid.uuid4()),
         "sender": session["user_id"],
         "message": msg,
     }
     send(payload, broadcast=True)
 
 if __name__ == '__main__':
     init_db()  # 앱 컨텍스트 내에서 테이블 생성