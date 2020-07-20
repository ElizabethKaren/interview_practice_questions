#write a funciton that takes in mom empty array of distinct integers 
#and an ineger representing a target sum 

array = [12,3,1,2,-6,5,-8,6]
targetSum = 6

#O(n)
def liner_time_sum(array, sum):
    nums = {}
    for num in array:
        opposite_of_pair = sum - num 
        if opposite_of_pair != num:
            nums[opposite_of_pair] = True

    for num in array: 
        if num in nums:
            return True 
    return False

#O(n2)
def n_squared_time(array,sum):
    all = []
    d = {}
    for num1 in array: 
        for num2 in array: 
            if num1 != num2:
                combined = num1 + num2 
                target = sum - combined
                if target != num2 and target != num1:
                    d[target] = [num1,num2]

    for num in array:
        if num in d:
            all.append(d[num] + [num])

    return all


#O(n3)
def does_multi_for_target_sum_exist(array,sum):
    for num in array:
        for num2 in array:
            y = sum - (num2+num)
            for num3 in array:
                if num != num3 and num != num2  and num2 != num3 and num3 == y:
                    return [num,num2,num3]
    return False 



print(n_squared_time(array, targetSum))