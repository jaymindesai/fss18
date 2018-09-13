from utils.test_rig import O
from w3.src.num import Num


@O.k
def test_num():
    nums = [4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174,
            190, 215, 225, 233, 250, 260, 270, 299, 300, 306,
            333, 350, 375, 443, 475, 525, 583, 780, 1000]

    num1 = Num().nums(nums)
    print('Mean 1: ', num1.mu)
    print('Standard Deviation 1: ', num1.sd)
    assert int(num1.mu) == 270
    assert int(num1.sd) == 231

    num2 = Num().nums(nums, lambda x: x * 2)
    print('Mean 2: ', num2.mu)
    print('Standard Deviation 2: ', num2.sd)
    assert int(num2.mu) == 540
    assert int(num2.sd) == 463



