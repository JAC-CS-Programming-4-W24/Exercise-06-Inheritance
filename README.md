# Exercise 6: Inheritance Practice

## 🎯 Objectives

- Practice inheritance in python.

## 1. Extending the Stack

- **Implement** extend the features of the basic Stack with the ability to push and pop multiple elements at a time.

Create a class called `StackMany` that supports the original stack operations with two new ones:


<!-- tabs:start -->

### **pushMany**

| Signature    | `push_many(elements: list[T])`                       |
| ------------ |------------------------------------------------------|
| Description  | Push multiple elements onto the stack in LIFO order. |
| Precondition | Stack has room for the number of elements.           |
| Mutator      | Yes.                                                 |
| Returns      | None.                                                |

### **popMany**

| Signature    | `pop_many(amount: int) -> list[T]`                  |
| ------------ |-----------------------------------------------------|
| Description  | Pop multiple elements from the stack in LIFO order. |
| Precondition | Stack has the number of elements, `amount > 0`.     |
| Mutator      | Yes.                                                |
| Returns      | The popped elements in LIFO order.                  |

<!-- tabs:end -->

### 🚦 Let's Go

Let's set this up:

1. Create a generic class called `StackMany` that extends our original `Stack` class.
2. Create an initializer with a provided `capacity`.
4. Implement the methods of the `StackMany` API: `push_many(..)` and `pop_many()`.
5. Throw exception `StackOverflowError` and `StackUnderflowError` when the caller has not met the operation preconditions.
6. Pass the unit tests in the file `test_stack_many.py`.

### 🔬 Observations

- The methods `push_many` and `pop_many` are only in a `StackMany` not in the super class `Stack`.

## 2. Extending the Queue

Create a class called `QueueDefault` that supports the original queue operations with and updated `dequeue()`:

- **Implement** extend the features of the basic Queue with the ability to dequeue an element regardless of whether the queue is empty of not.

<!-- tabs:start -->

### **dequeue**

| Signature    | `dequeue() -> T`                                                                                |
|--------------|----------------------------------------------------------------------------------------------|
| Description  | Remove and return an element from the queue in FIFO order, or a default value if it's empty. |
| Precondition | None.                                                                                        |
| Mutator      | Yes.                                                                                         |
| Returns      | The removed element of the default value.                                                    |

<!-- tabs:end -->

### 🚦 Let's Go

Let's set this up:

1. Create a class called `QueueDefault` that extends our original `Queue` class.
2. Create an initializer with a provided `capacity` and a default value.
4. Implement the methods of the `Queue` API: `dequeue()` and any other methods.
5. Throw exception `QueueOverflowException` and `QueueUnderflowException` when the caller has not met the operation preconditions.
6. Pass the unit tests in the file `test_queue_default.py`.

### 🔬 Observations

- The methods `dequeue()` is an override of the one in the super-class, but the original functionality is still required! This is very common in inheritance.
- The `is_empty()` method doesn't seem relevant in the `QueueDefault`. Because it's in the super-class, we need to handle the behaviour in the sub-class.









