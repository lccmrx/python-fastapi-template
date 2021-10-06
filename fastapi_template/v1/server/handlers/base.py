from abc import ABC, abstractmethod

class AbstractHandler(ABC):
    
    @abstractmethod
    @classmethod
    def get(): pass

    @abstractmethod
    @classmethod
    def list(): pass
    
    @abstractmethod
    @classmethod
    def create(): pass
    
    @abstractmethod
    @classmethod
    def update(): pass
    
    @abstractmethod
    @classmethod
    def delete(): pass
