import pytest
import av.ambisonic_decode as mod

CASES = [
    ("head_predict", (1,)),
    ("order_crossfade", (1,)),
    ("matrix_normalize", (1,)),
    ("metadata_route", (1,)),
    ("decode_thread", (1,)),
    ("device_layout", (1,)),
    ("load_bed", (1,)),
    ("decode", (1,)),
    ("binaural", (1,)),
    ("present", (1,)),
    ("validate_ambisonics", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
