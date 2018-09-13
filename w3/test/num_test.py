from utils.test_rig import O
from w3.src.num import Num


@O.k
def test_num():
    nums = [4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174,
            190, 215, 225, 233, 250, 260, 270, 299, 300, 306,
            333, 350, 375, 443, 475, 525, 583, 780, 1000]

    num = Num().nums(nums)
    print('Mean: ', num.mu)
    print('Standard Deviation: ', num.sd)
    assert int(num.mu) == 270
    assert int(num.sd) == 231

