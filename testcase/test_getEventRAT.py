import pytest
from RequestApi import API


class Test_getEventRAT:

    def test_case(self):
        path = "/api/oneMap/getEventRAT"
        s = API()
        s1 = s.sendAPI("post", path)
        print(s1)
        msg1=s1["success"]

        assert msg1 == True
if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_getEventRAT.py'])