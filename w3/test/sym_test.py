from utils.test_rig import O
from w3.src.sym import Sym


@O.k
def test_sym():
    syms = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n']

    sym1 = Sym().syms(syms)
    print('Entropy 1: ', sym1.sym_ent())
    assert round(sym1.sym_ent(), 4) == 0.9403

    sym2 = Sym().syms(syms, lambda x: 'a')
    print('Entropy 2: ', sym2.sym_ent())
    assert round(sym2.sym_ent(), 4) == 0.0
