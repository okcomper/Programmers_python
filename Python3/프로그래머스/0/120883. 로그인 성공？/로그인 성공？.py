def solution(id_pw, db):
    answer = ''
    
    input_id, input_pw = id_pw
    
    for member_info in db:
        db_id, db_pw = member_info
        if input_id == db_id:
            if input_pw == db_pw:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"
    
 