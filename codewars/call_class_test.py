class TestCall:
    def __call__(self):
        print(self, "Test")

test_call = TestCall()
test_call()