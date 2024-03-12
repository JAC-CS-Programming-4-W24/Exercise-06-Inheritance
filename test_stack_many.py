import pytest

from our_stack import StackUnderflowError, StackOverflowError


class StackMany:
    pass  # TODO


@pytest.fixture
def stack() -> StackMany[str]:
    stack: StackMany[str] = StackMany(10)
    return stack


def test_stack_is_super_class(stack):
    assert stack.is_empty()
    # check that push and pop still work
    stack.push("and")
    assert "and" == stack.pop()


def test_stack_many_push(stack):
    stack.push_many("for something completely different".split(" "))
    assert "different" == stack.pop()
    assert "completely" == stack.pop()
    assert "something" == stack.pop()
    assert "for" == stack.pop()


def test_stack_many_pop(stack):
    stack.push("something")
    stack.push("completely")
    stack.push("different")
    assert "different completely something".split(" ") == stack.pop_many(3)


def test_stack_many_pop_illegal_amount(stack):
    with pytest.raises(Exception):
        stack.pop_many(-1)


def test_stack_many_underflow(stack):
    with pytest.raises(StackUnderflowError):
        stack.push_many("a b c".split(" "))
        stack.pop_many(4)


def test_stack_many_overflow(stack):
    with pytest.raises(StackOverflowError):
        stack.push_many("a b c d e f g h i j k l".split(" "))
