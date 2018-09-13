from utils.test_rig import O
from w3.src.sym import Sym


@O.k
def test_sym():
    syms = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n']

    sym = Sym().syms(syms)
    print('Entropy: ', sym.sym_ent())
    assert round(sym.sym_ent(), 4) == 0.9403

