# encoding=utf-8
import itertools
import random as rd

def get_24point(nums,target):
    def part1(nums,target):
        iis = list(itertools.permutations(nums,4))
        for ii in iis:
            indexs = set(range(len(ii)))
            for index in list(itertools.combinations(indexs,2)):
                left_index = tuple(indexs - set(index))
                num1 = ii[index[0]]
                num2 = ii[index[1]]
                num3 = ii[left_index[0]]
                num4 = ii[left_index[1]]
                for operate1 in ['+','-','*','/']:
                    try:
                        num11 = eval('{}{}{}'.format(num1,operate1,num2))
                    except:
                        pass
                    for operate2 in ['+','-','*','/']:
                        try:
                            num22 = eval('{}{}{}'.format(num3,operate2,num4))
                        except:
                            pass
                        for operate3 in ['+','-','*','/']:
                            try:
                                result = eval('{}{}{}'.format(num11,operate3,num22))
                            except:
                                pass
                            if result == target:
                                print('({}{}{}){}({}{}{})={}'.format(num1,operate1,num2,operate3,num3,operate2,num4,target))
                            else:
                                pass
    def part2(nums,target):
        iis = list(itertools.permutations(nums,4))
        for ii in iis:
            num1 = ii[0]
            num2 = ii[1]
            num3 = ii[2]
            num4 = ii[3]
            for operate1 in ['+','-','*','/']:
                num11 = eval('{}{}{}'.format(num1,operate1,num2))
                for operate2 in ['+','-','*','/']:
                    num22 = eval('{}{}{}'.format(num11,operate2,num3))
                    for operate3 in ['+','-','*','/']:
                        result = eval('{}{}{}'.format(num22,operate3,num4))
                        if result == target:
                            print('(({}{}{}){}{}){}{}={}'.format(num1,operate1,num2,operate3,num3,operate2,num4,target))
                        else:
                            pass
    try:
        part1(nums,target)
    except:
        print('(A---B) --- (C---D) cannot reach {}'.format(target))
    try:
        part2(nums,target)
    except:
        print('((A---B) --- C )---D) cannot reach {}'.format(target))

if __name__ == '__main__':
    get_24point(nums=[rd.randint(1, 10) for i in range(4)], target=24)
