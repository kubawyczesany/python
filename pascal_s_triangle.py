#The code will print the pascal's triangle on the screen.


def pascal(p):
    if p == 1:
        return [[1]]
    else:
        _list = [[1], [1, 1]]
        tmp_list = None
        for i in range(2, p):
            new_list = []
            if i == 2:
                new_list = [1, 2, 1]
                tmp_list = new_list
            else:
                for i in range(len(tmp_list)):
                    if i == len(tmp_list)-1:
                        break
                    new_list.append(tmp_list[i] + tmp_list[i+1])
                tmp_list = [1] + new_list + [1]
            _list.append(tmp_list)
        return _list


if __name__ == '__main__':
print(pascal(5))
