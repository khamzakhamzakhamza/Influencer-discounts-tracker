from typing import Generic, TypeVar
from idt_scrapper.domain.entities.influencer import Influencer

T = TypeVar("T")

class ScanningError(Exception, Generic[T]):
    def __init__(self, entity: T, operation: str):
        message = f"Failed to scan {entity} during {operation} operation"
        super().__init__(message)
