from dataclasses import dataclass


@dataclass
class FileData:
    file_name: str
    file_data: bytes
