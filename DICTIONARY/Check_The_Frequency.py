test_dict = {'Codingal':2, 'is' :2, 'best':2, 'for':2, 'Coding':1}

print("The Original Dictionary : " + str(test_dict))

K=2

res = 0
for key in test_dict:
    if test_dict [key]==K:
        res+=1

print("The Frequency Of \'K\' is: " + str(res))
