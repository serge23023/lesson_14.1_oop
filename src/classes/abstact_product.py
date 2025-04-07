from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @classmethod
    @abstractmethod
    def create_product(cls, new_product: dict, product_list: list = None):
        pass  # pragma: no cover

    @abstractmethod
    def __init__(self):
        pass  # pragma: no cover

    @abstractmethod
    def __add__(self, other):
        pass  # pragma: no cover

    @abstractmethod
    def __str__(self):
        pass  # pragma: no cover

    @abstractmethod
    def __repr__(self):
        pass  # pragma: no cover
