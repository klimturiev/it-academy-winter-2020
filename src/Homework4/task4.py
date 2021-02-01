lst1_ = [1, 2, 3, 2, 1, 2]
lst2_ = [1, 2, 3, 6, 7, 4]
set1_ = set(lst1_)
set2_ = set(lst2_)
common_set = set1_ ^ set2_
print(len(common_set))