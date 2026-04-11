from abc import abstractmethod, ABC


class IEntity(ABC):
    @classmethod
    @abstractmethod
    def get_collection(cls) -> str:
        # todas as classes que implementarem IEntity, vão ser obrigados a declarar a collection
        pass

    def to_dict(self) -> dict: pass
