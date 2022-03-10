from locale import normalize
from normal_queue import NormalQueue

test_queue = NormalQueue()
test_queue.updateQueue()
test_queue.updateQueue()

print(test_queue.callCustomer(5))
