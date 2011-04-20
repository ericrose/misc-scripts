from random import randrange

def in_list(low_index, high_index, search_key, rot_sort_array):
   if low_index >= high_index:
     return rot_sort_array[high_index] == search_key
   else:
     pivot = ((high_index - low_index) / 2) + low_index
     if rot_sort_array[pivot] == search_key:
       return True
     else:
       if rot_sort_array[low_index] < rot_sort_array[pivot]:
         if rot_sort_array[low_index] <= search_key and search_key < rot_sort_array[pivot]:
           return in_list(low_index, pivot -1, search_key, rot_sort_array)
         else:
           return in_list(pivot + 1, high_index, search_key, rot_sort_array)
       else:
         if rot_sort_array[high_index] >= search_key and search_key > rot_sort_array[pivot]:
           return in_list(pivot + 1, high_index, search_key, rot_sort_array)
         else:
           return in_list(low_index, pivot -1, search_key, rot_sort_array)

def rotate_list(a_list):
    return a_list[1:] + [a_list[0]]

def rotate13(a_list):
    l = a_list
    for ndx in range(13):
      l = rotate_list(l)
    return l

def find_in_list(key, l):
    return in_list(0,len(l)-1,key, l)

if __name__ == "__main__":
    x = [5, 1, 1, 1, 2, 2, 3, 4]
    for i in range(randrange(len(x))):
       x = rotate_list(x)
    print(x)
    assert in_list(0,len(x) -1,4,x)
    y = [3,4,5,1,2]
    assert in_list(0,len(x) -1,4,x)
    assert not in_list(0,len(x) -1,10,x)
    x = range(0,1000,2)
    assert not in_list(0,len(x) -1, 3, x)
    assert not in_list(0,len(x) -1, 678, x)

