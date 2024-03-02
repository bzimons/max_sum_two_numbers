# solution:
def solution(A):
    list_sum_A_pairs = [sum(int(x) for x in str(number)) for number in A]
    repeated_elements = [x for i, x in enumerate(list_sum_A_pairs) if
                         list_sum_A_pairs.count(x) > 1 and list_sum_A_pairs.index(x) < i]
    if len(repeated_elements)==0:
        result = -1
    else:
        result = 0
        for j in repeated_elements:
            position_list = [i for i, x in enumerate(list_sum_A_pairs) if x == j]
            which_A_to_sum = [A[i] for i in position_list]
            which_A_to_sum = sorted(which_A_to_sum,reverse = True)[slice(2)]
            result_new = sum(which_A_to_sum)
            if result<result_new:
                result = result_new
            else:
                result = result
    return (result)

# testing:
my_list = [51,71,17,42]
my_list2 = [42,33,60]
my_list3 = [51,32,43]
my_list4 = [12,21,2,2]

print(solution(my_list))
print(solution(my_list2))
print(solution(my_list3))
print(solution(my_list4))


