
class Solution:

  def dailyTemperatures(self, T: List[int]) -> List[int]:
    if len(T) == 0:
      return []

    max = T[len(T) - 1]
    ans = [0] * len(T)

    # cycle from end to start
    for i in range(len(T) - 1, -1, -1):
      value = T[i]

      if value < max:
        # index for checking
        nearestIndex = i + 1
        # check next value more then current temperature
        while T[nearestIndex] <= T[i]:
          # !!! the main speed improvement !!!
          # dynamic programming - get ans from previous steps
          nearestIndex += ans[nearestIndex]
        ans[i] = nearestIndex - i

      if value > max:
        max = value
