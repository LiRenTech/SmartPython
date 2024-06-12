from a_class import A
from b_class import B
from abc import ABC, abstractmethod


class Factory(ABC):

    @staticmethod
    @abstractmethod
    def get_system_performance() -> int:
        pass

    # SYSTEM_PERFORMANCE = 1000
    # SYSTEM_MEMORY = 1000000000
    # SYSTEM_DISK = 1000000000000
    # SYSTEM_CPU = 10


class AFactory(Factory):
    @staticmethod
    def get_system_performance() -> int:
        return 10010

    SYSTEM_PERFORMANCE = 1001

    @staticmethod
    def get_normal_instance():
        result = A(1, 1.3, 'hello', [1, 2], {'a': 1, 'b': 2})
        result.d = [i * AFactory.get_system_performance() for i in result.d]
        return result

    @staticmethod
    def get_strange_instance():
        result = A(2, 123456789, 'python', [5, 6], {'e': 5, 'f': 6})
        result.d = [i * AFactory.SYSTEM_PERFORMANCE for i in result.d]
        return result

    @staticmethod
    def get_happy_instance():
        result = A(2, 123456789, 'python', [5, 6], {'e': 5, 'f': 666})
        result.d = [i * AFactory.SYSTEM_PERFORMANCE for i in result.d]
        return result

    @staticmethod
    def get_biggest_instance():
        result = A(2, float('inf'), 'python', [5, 6], {'e': 5, 'f': 666})
        result.d = [i * AFactory.SYSTEM_PERFORMANCE for i in result.d]
        return result


class BFactory(Factory):

    @staticmethod
    def get_system_performance() -> int:
        return 15

    @classmethod
    def get_normal_instance(cls):
        return B(15 * BFactory.get_system_performance())

    @staticmethod
    def get_biggest_instance():
        return B(999 * BFactory.get_system_performance())
