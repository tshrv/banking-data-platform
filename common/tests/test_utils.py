from common.utils import ping


async def test_ping():
    resp = ping("BDP")
    assert resp == "Hi! BDP", "Failed ping utils"
