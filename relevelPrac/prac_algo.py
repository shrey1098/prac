def get_input_stacks():
    n = int(input())
    stacks = []
    for _ in range(n):
        k = int(input())
        str_stack = input().split(' ')
        stack = [int(s) for s in str_stack]
        stacks.append(k)
        stacks.append(stack)
    return stacks


def check(list) -> list:
    for i in list:
        final_list = []
        final_list.clear()
        try:
            for j in i:
                if j % 2 == 1:
                    pass
                else:
                    if j % 3 == 0:
                        final_list.append(j)

            if len(final_list) == 0:
                print('EMPTY')

            else:
                print(*final_list, sep=' ')
        except TypeError:
            pass


check(get_input_stacks())
