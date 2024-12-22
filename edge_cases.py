# Edge cases I should have known, have forgotten, or found uninteresting

from datetime import datetime

def is_empty(x) -> None:
    print(f"{x} is {'non-empty' if x else 'empty'}.")

if __name__=='__main__':
    is_empty([1, '2', 3, True])
    is_empty([])
    is_empty(datetime.now())
    is_empty(None)
    is_empty(not None)
    a = []
    is_empty(a or [])
    is_empty(a and [])
    is_empty(list())
    is_empty(dict())
    is_empty(dict() or datetime.now())
    b = [1, '2', False]
    is_empty(b or datetime.now())
    is_empty(datetime.now() or b)
    is_empty(b and datetime.now())
    is_empty(True and datetime.now()) # Sonar lint objects to the constant "True"
