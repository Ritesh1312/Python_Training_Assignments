from utils import result_as_dict



def get_all_authors(cursor):
    cursor.execute('select * from Authors')
    results=result_as_dict(cursor)
    for result in results:
        print(result)

def remove_author(cursor,id):
    query = 'DELETE from Authors where authorid=?'
    cursor.execute(query,id)
    print(f'{id} Deleted')

def add_author(cursor,id,name,bio):
    query = 'insert into Authors (authorid,name,bio) VALUES (?,?,?)'
    cursor.execute(query,id,name,bio)
    print(f'{id} Added')

def author_by_id(cursor,id):
    cursor.execute('select * from Authors where authorid=?',id)
    results= result_as_dict(cursor)
    for res in results:
            print(res)

def update_author(cursor,id,name=None,bio=None):
    if name != None and bio!=None:
        cursor.execute(f'UPDATE Authors SET name = {name}, bio = {bio} WHERE authorid = {author_by_id}')
        print(f'{id} is updated with name {name} and bio {bio}')
    elif name==None and bio!=None:
        cursor.execute(f'UPDATE Authors SET bio= {bio} WHERE authorid= {id}')
        print(f'{id} is updated with bio {bio}')
    elif bio==None and name!=None:
        cursor.execute(f'UPDATE Authors SET name= {name} WHERE authorid={id}')
        print(f'{id} is updated with name {name} ')

def get_author_review(cursor,id):
    cursor.execute('''SELECT B.title, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE B.authorid = ?''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)


    