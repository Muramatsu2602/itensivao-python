from locale import normalize
from normal_queue import NormalQueue
from priority_queue import PriorityQueue

# test_queue = NormalQueue()
# test_queue.updateQueue()
# test_queue.updateQueue()

# print(test_queue.callCustomer(5))


test_queue2 = PriorityQueue()
test_queue2.update_queue()
test_queue2.update_queue()
test_queue2.update_queue()

print(test_queue2.call_customer(10))
print(test_queue2.call_customer(1))
print(test_queue2.statistics('10/01/2022', 187, 'detail'))
