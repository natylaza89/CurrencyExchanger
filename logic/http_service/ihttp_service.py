from abc import ABC, abstractmethod


class IHTTPService(ABC):
    """
    Abstract Factory for HTTP Requests (API):
    This Factory Can be extended for future Sub Classes with different api usage.
    """
    @abstractmethod
    def get_request(self) -> Exception:
        raise NotImplementedError

    @abstractmethod
    def post_request(self) -> Exception:
        raise NotImplementedError

    @abstractmethod
    def url_query(self) -> Exception:
        raise NotImplementedError

            