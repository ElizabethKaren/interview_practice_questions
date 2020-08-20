#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed, the only constraint
#stopping you from robbing each of them is that adjacent houses have
#security system connected and it will automatically contact the police 
#if two adjacent houses were broken into on the same night.
#Given a list of non-negative integers representing the amount of money of 
#each house, determine the maximum amount of money you can rob tonight without
#alerting the police.

nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
# nums = [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#Total amount you can rob = 2 + 9 + 1 = 12.
# nums =[2,1,1,2]

def robbing_houses(nums):
    money = 0
    count = 0
    while count < len(nums)-1:
        if nums[count] > nums[count+1] and nums[count] > nums[count-1]:
            money += nums[count]
        else:
            money += nums[count+1]
    
    return money

# def robbing_houses(nums):
#     odds_total = 0
#     evens_total = 0
#     odds_count = 1
#     evens_count = 0
    
#     while odds_count < len(nums):
#         odds_total += nums[odds_count]
#         odds_count += 2
        
#     while evens_count < len(nums):
#         evens_total += nums[evens_count]
#         evens_count += 2
    
#     if odds_total == evens_total:
#         money = 0
#         count = 0
#         while count < len(nums):
#             add = max(nums[count], nums[count-1], nums[count-2])
#             money += add
#             count += 2
#         return money
            
#     if odds_total > evens_total:
#         return odds_total
#     else:
#         return evens_total


print(robbing_houses(nums))