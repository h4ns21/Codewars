# First solution

def sort_array(source_array):
    sorted_odds = sorted([i for i in source_array if i % 2 != 0])  # sort odd numbers in ascending order
    new_list = []  # creating a new list
    for i in source_array:
        if i % 2 != 0:
            new_list.append(sorted_odds.pop(0))  # appending the sorted odd numbers
        else:
            new_list.append(i)  # appending the even numbers
    return list(new_list)
  
  # Second solution
  
  def sort_array(source_array):
  odds = sorted((i for i in source_array if i % 2 != 0), reverse=True)
  return [i if i % 2 == 0 else odds.pop() for i in source_array]
