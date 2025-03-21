from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class ScanningError(Exception, Generic[T]):
    def __init__(self, entity: T, operation: str, inner_exception: Optional[Exception] = None):
        self.inner_exception = inner_exception
        message = f"Failed to scan {entity} during {operation} operation"
        super().__init__(message)
