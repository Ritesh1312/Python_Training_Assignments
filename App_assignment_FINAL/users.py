from utils import result_as_dict

def get_all_users(cursor):
    cursor.execute('select * from REVIEWS')
    results=result_as_dict(cursor)
    for res in results:
            print(res)
    
def add_new_user(cursor,id,name,password):
    query = 'insert into Users (userid,username,password) values (?,?,?)'
    cursor.execute(query,id,name,password)

def get_user_review(cursor,id):
    query = '''SELECT R.userid,B.title, R.rating, R.review_text
                    FROM Reviews R
                    JOIN Books B ON R.bookid = B.bookid
                    WHERE R.userid = ?;'''
    cursor.execute(query,id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)