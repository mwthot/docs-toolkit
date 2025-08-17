"""Core Document model for docs-toolkit.

This module defines the fundamental Document class that serves as the
primary data structure throughout the toolkit. This is a forever contract -
external code will depend on this structure.
"""
from pathlib import Path 
from typing import Any, Dict 

class Document: 
    """The fundamental unit of documentation processing.
    
    A Document represents a single file with its content and associated metadata. 
    This minimal structure is designed to be extended through the metadata
    dictionary rather than through subclassing. 

    Attributes: 
        path: The filesystem path to the document. 
        content: The text content of the document. 
        metadata: Extensible dictionary for any additional information. 
    """

    def __init__(
        self, 
        path: Path,
        content: str, 
        metadata: Dict[str, Any] = None
    ):
        """Initialize a Document."""
        self.path = path 
        self.content = content 
        self.metadata = metadata if metadata is not None else {}

    def __repr__(self) -> str: 
        """Return a readable representation of the Document."""
        return f"Document(path={self.path}, content_length={len(self.content)}, metadata_keys={list(self.metadata.keys())})"

    def __str__(self) -> str: 
        """Return a string representation showing the path."""
        return f"Document({self.path})"