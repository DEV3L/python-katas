from pytest import mark

from app.transformers.transform_str import sha_str

@mark.parametrize('expected_value, value', [
    ('da39a3ee5e6b4b0d3255bfef95601890afd80709', ''),
    ('b858cb282617fb0956d960215c8e84d1ccf909c6', ' '),
    ('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3', 'test'),
])
def test_sha_str(expected_value, value):
    assert expected_value == sha_str(value)
