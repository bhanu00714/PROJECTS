#reverse a list and return only the even indexed elements in a list
#list1 = list(map(int,input("enter numbers with a space: ").split()))
#list1 = [8,4,5,62,5]
#print(list1)
#rev_list = list1[::-1][::2]
#print(rev_list)
#print([rev_list[x] for x in range(len(rev_list)) if x%2 == 0])

# t = (1, 2, [3, 4])
# Can you change the value 4 to 99? How, if tuple is immutable?
# Modify the tuple to become: (1, 2, [3, 99])
# t[2][1] = 99
# print(t)

# words = ["banana", "apple", "cherry", "blueberry"]
# Sort this list by length of words in descending order (longest first)
# Expected output: ['blueberry', 'banana', 'cherry', 'apple']
# length = [len(s) for s in words]
# new_list = []
# print(words,"\n",length)
# for i in range(len(length)):
#     new_list.append(words[length.index(max(length))])
#     length[length.index(max(length))] = 0
# print(new_list)


# nums = [1, 2, 3, 4, 3, 5, 3, 6]
# # Remove all occurrences of 3 and insert 99 at the index where the first 3 was found
# # Final output should be: [1, 2, 99, 4, 5, 6]
# for i in range(len(nums)):
#     if nums[i] == 3:
#         nums[i] = 99
#         break
# for i in nums:
#     if i == 3:
#         nums.remove(i)
# print(nums)

data = (10, 20, 30, 40, 50,8,6,4,00,8,6)
# Without converting the tuple to a list, print the second last item using negative indexing
# Then reverse the tuple and store it in a new variable (you can’t modify it directly)
print(data)
print(data[-2])
listt = list(data)
for i in range(len(listt)//2):
    temp = listt[i]
    listt[i] = listt[-1-i]
    listt[-1-i] = temp
print(tuple(listt))
