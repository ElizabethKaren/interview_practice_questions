# Given the array candies and the integer extraCandies
#where candies[i] represents the number of candies that 
#the ith kid has.
#For each kid check if there is a way to distribute 
#extraCandies among the kids such that he or she 
#can have the greatest number of candies among them. 
#Notice that multiple kids can have the greatest number 
#of candies.

# candies = [2,3,5,1,3]
# extraCandies = 3
#Output: [true,true,true,false,true]

candies = [12,1,12]
extraCandies = 10
# Output: [true,false,true]

def kids_w_candy(candies, extraCandies):
    most_candy = max(candies)
    for index in range(len(candies)):
        candy_w_extra = candies[index] + extraCandies
        if candy_w_extra >= most_candy:
            candies[index] = True
        else:
            candies[index] = False

    return candies


print(kids_w_candy(candies,extraCandies))