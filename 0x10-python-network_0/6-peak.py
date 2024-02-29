#!/usr/bin/python3
def find_peak(list_of_integers):
  """
  Finds a peak element in a list of unsorted integers.

  Args:
      list_of_integers: A list of integers.

  Returns:
      The first peak element found in the list, or None if no peak is found.
  """

  # Handle empty list
  if not list_of_integers:
    return None

  # Handle lists with one element
  if len(list_of_integers) == 1:
    return list_of_integers[0]

  # Recursive binary search approach
  def _find_peak_helper(low, high):
    if high - low == 1:
      return list_of_integers[low] if list_of_integers[low] > list_of_integers[high] else list_of_integers[high]

    mid = (low + high) // 2

    if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
      return list_of_integers[mid]
    elif list_of_integers[mid] <= list_of_integers[mid - 1]:
      return _find_peak_helper(low, mid - 1)
    else:
      return _find_peak_helper(mid + 1, high)

  return _find_peak_helper(0, len(list_of_integers) - 1)
