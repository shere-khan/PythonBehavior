def change_list(list):
    list.append(6)
    print("change_list: ", list)


def change_var(x):
    x = 5
    print("change_val x: ", x)


def function_test(*args, **kwargs):
    for a in args:
        print('args: ', a)

    for k in kwargs:
        print('kwargs key {0} val {1}'.format(k, kwargs[k]))


if __name__ == '__main__':
    # y = 7
    # print("y before change_val: ", y)
    # change_var(y)
    # print("y after change_val: ", y)
    #
    # a = [3, 2, 1]
    # print("list before change_list", a)
    # change_list(a)
    # print("list after change_list", a)

    function_test(a='first arg', b='second arg', c='third arg')

    string = 'justin'
    print(string[:1])
    print(string[1:])
