import sys
from sqlalchemy.exc import SQLAlchemyError
from database.repository import get_user, get_all_todos, create_todo, update_todo, remove_todo, close_connection



def main(user):
    MENU = """
        What would you like to do?
        #1 create a task
        #2 list all of the tasks
        #3 update the task
        #4 remove the task
        #5 menu
        #6 exit
    """
    while True:
        print(MENU)
        choice = int(input(">>> "))
        match choice:
            case 1:
                title = input("title >>> ")
                description = input("description >>> ")
                create_todo(title=title, description=description, user=user)
            case 2:
                todos = get_all_todos(user)
                for t in todos:
                    print(t.id, t.title, t.description, t.user.login)
            case 3:
                _id = input("Enter user id >>> ")
                title = input("title >>> ")
                description = input("description >>> ")

                t = update_todo(_id=_id, title=title, description=description, user=user)
                print(t.id, t.title, t.description, t.user.login)
            case 4:
                _id = input("Enter user id >>> ")
                r = remove_todo(_id=_id, user=user)
                print(f'Result: {bool(r)}')
            case 5:
                print(MENU)
            case 6:
                break
            case _:
                print("Not an option!")
        


if __name__ == '__main__':
    login = input("login >>> ")
    password = input("password >>> ")
    try:
        user = get_user(login)
    except:
        print("User does not exists. Please register")
        close_connection()
        sys.exit()

    if password == user.password:
        try:
            main(user)
        except SQLAlchemyError as err:
            print(err)
        finally:
            close_connection()
    else:
        print('Wrong password!')


