from abc import ABC, abstractmethod


class IFileHandler(ABC):
    """
    Abstract Factory for Files Handler:
    This Factory Can be extended for future Sub Classes with different files handlers
    like PDF, CSV etc.
    """
    @abstractmethod
    def parse_file_headers(self) -> Exception:
        raise NotImplementedError

    @abstractmethod
    def parse_file_data(self) -> Exception:
        raise NotImplementedError

    @abstractmethod
    def file_path(self) -> Exception:
        raise NotImplementedError