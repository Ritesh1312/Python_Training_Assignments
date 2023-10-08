# def supress_exception(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except KeyError:
#             return False
#     return inner

# @supress_exception
# def authentication(user_info):
    



def supress_exception( *args, exception, result, **kwargs):
    def decorator(func):
        def inner(*fn_arg, **fn_kwarg):
            print(fn_arg,fn_kwarg)
            try:
                res = func(*fn_arg, **fn_kwarg)
                return res
            except exception:
                return result
            except Exception as ex:
                raise ex
                # print(ex)
        return inner
    return decorator

@supress_exception(exception = KeyError, result = False)
def authenticate(user,password):
    print(f'Authenticating {user}')
    if users[user] == password:
        print(" Verifiied ")


users = {'a':'Ritesh', 'b':12345}

authenticate('Ritesh',12345)