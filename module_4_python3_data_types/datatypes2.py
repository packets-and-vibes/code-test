# n = 100
# if n < 50:
#     print('The number is less than 50')
# elif n == 50:
#     print('The number is equal to 50')
# else:
#     print('The number is greater than 50')

code = 200
match code:
    case 404:
        print('Not Found')
    case 401:
        print('Unauthorized - please authenticate')
    case 403:
        print("Forbidden - you don't have permission to access this resource")
    case 200:
        print("Success")
