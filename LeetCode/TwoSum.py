import time
import datetime

def twoSum(nums, target):
    start = time.time()
    # filter를 통해 뒤에 오는 숫자가 많으면 제거 후 index() 값을 구하는게 빨라질꺼 같아서 적용해보았지만 
    # 주어진 nums 배열에서는 속도 차이가 없었습니다.
    # nums = list(filter(lambda x: x < target, nums))

    for i, num in enumerate(nums):
        n = target - num
        if n in nums[i + 1:]:
            # 걸린 시간: 0:00:00.000013
            # return [i, nums.index(n)]
            # 위에 코드는 Example 3에서 [3, 3] 배열에서 2번째 인덱스 값이 틀리게 계산됩니다.
            # 이유는 값은 값이 있을 때 index() 함수는 가장 먼저 같은 값으로 있는 index를 return 해주기 때문입니다.

            # 걸린 시간: 0:00:00.000013
            # 시간복잡도:O(n^2)
            # nums.index(n)으로 구한 것과 시간 차이가 없읍니다.
            # nums의 i + 1 부터 검색하여 n 숫자의 index를 구하고 i만큼 빼고 index를 구했으니 다시 i의 값을 더해줍니다.
            # 그리고 나서 i가 0일 수 있으니 1을 더해줍니다.
            return [i, nums[i + 1:].index(n) + i + 1]

    end = time.time()
    sec = (end - start)
    sec = datetime.timedelta(seconds=sec)
    print(sec)

def twoSum_dict(nums, target):
    start = time.time()

    dict = {}
    for i, num in enumerate(nums):
        dict[num] = i

    #타겟에서 첫번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in dict and dict[target - num] != i:
            # 걸린시간: 0:00:00.000001
            # 시간복잡도:O(1)
            # print([i, dict[target - num]])
            return [i, dict[target - num]]

    end = time.time()
    sec = (end - start)
    sec = datetime.timedelta(seconds=sec)
    print(sec)


nums = [2,7,11,15] 
target = 9
# nums = [3, 3]
# target = 6
twoSum(nums, target)