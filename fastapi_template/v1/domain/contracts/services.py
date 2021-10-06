from abc import ABCMeta, abstractmethod

class User(metaclass=ABCMeta):
    __crypto__: dict = None
    __database__: dict = None
    
    @abstractmethod
    def create(): pass

    @abstractmethod
    def delete(): pass
