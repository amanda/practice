'''
Flavius Joseph: Write a program that returns a list of n people, 
numbered from 0 to n-1, in the order in which they are executed.
5 people [0 1 2 3 4], every 2 flavius(5, 2) returns [1 3 0 4 2]
'''

class Queue():
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.insert(0, val)

    def dequeue(self):
        return self.q.pop()

    def is_empty(self):
        return self.q == []

    def __str__(self):
        return ' '.join(list(str(i) for i in self.q))


def flavius(people, n):
    '''(int) -> int, number of people, every nth person to die'''
    death = Queue()
    order = []
    for _ in range(people):
        death.enqueue(_) # 5 -> [4, 3, 2, 1, 0]
    while not death.is_empty():
        for _ in range(n-1):
            death.enqueue(death.dequeue())
        order.append(death.dequeue())
    return order
    

if __name__ == '__main__':
    print flavius(10, 3)
