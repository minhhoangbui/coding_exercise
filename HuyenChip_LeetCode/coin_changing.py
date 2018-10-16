'''
An implementation of minimum coin changing in Python 2
'''
_MAX = 1000

def solve_minimum_coin_changing(total_value, coin_list):

    def MC(value):
        temp = []
        if value == 0:
            return 0
        elif value < min(coin_list):
            return _MAX
        else:
            for i in range(len(coin_list)):
                temp.append(MC(value - coin_list[i]) + 1)
            return min(temp)
    
    result = MC(total_value)
    if result >= _MAX:
        print('There is no solution to that')
    else:
        return result

if __name__ == '__main__':
    coins = [9, 6, 5, 2]
    total_value = 1
    result = solve_minimum_coin_changing(total_value, coins)
    print result