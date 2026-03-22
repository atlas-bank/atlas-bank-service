from abc import abstractmethod, ABC


class IEntity(ABC):
    @abstractmethod
    def get_collection(self) -> str:
        # todas as classes que implementarem IEntity, vão ser obrigados a declarar a collection
        pass

    def to_dict(self) -> dict: pass
