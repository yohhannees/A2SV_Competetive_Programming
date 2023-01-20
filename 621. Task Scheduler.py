class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:

    ans = []
    obj = {}

    for i, task in enumerate(tasks):
      # print(i, task)
      if task not in obj:
        obj[task] = 1
      else:
        obj[task] += 1

    # for key in obj.keys():
    #   print('key %s, number %d' % (key, obj[key]))

    innerCount = 0
    tookTask = {}

    # while len(obj.keys()) > 0:
    while len(obj.keys()) > 0:
      # print('len %d' % len(obj.keys()))

      if innerCount <= n:
        # sort keys from higher to lower
        keys = sorted(list(obj.keys()), key=lambda key: obj[key], reverse=True)

        for key in keys:
          # print('key %s %d' % (key, obj[key]))
          if innerCount > n:
            break

          if key not in tookTask:
            innerCount += 1
            tookTask[key] = 1
            ans.append(key)
            obj[key] -= 1

        for key in keys:
          # print('check key %s' % key)
          if obj[key] <= 0:
            # print('delete %s' % key)
            del obj[key]

        if len(obj.keys()) > 0:
          if innerCount < n + 1:
            # print('append %d' % (n - innerCount))
            for i in range(innerCount, n + 1):
              innerCount += 1
              ans.append('idle')

      else:
        tookTask = {}
        innerCount = 0

    # print(ans)

    return len(ans)
