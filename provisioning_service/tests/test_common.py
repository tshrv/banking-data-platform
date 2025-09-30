from common import ping


async def test_common():
    resp = ping("BDP")
    assert resp == "Hi! BDP", "Failed common package"
