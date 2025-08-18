"""Document loader for docs-toolkit. 

This module provides simple file loading functionality to create Document 
instances from filesystem files. This is NOT a forever contract. We can 
(and will) evolve loading strategies as we learn more about needs.
"""
from pathlib import Path 
from typing import Optional 

from docs_toolkit.core.document import Document

def load_document(path: Path, encoding: str = "utf-8") -> Document: 
    """Load a file from disk and create a Document instance. 

    This is the simplest possible implementation - read the entire file 
    into memory as a string. This works well for documentation files 
    which are typically small (KB to low MB). 

    Args: 
        path: Path to the file to load. 
        encoding: Text encoding to use (default: utf-8). 

    Returns: 
        A Document instance with the file's content. 

    Raises: 
        FileNotFoundError: If the file doesn't exist. 
        IsADirectoryError: If the path points to a directory. 
        UnicodeDecodeError: If the file can't decoded with the specified encoding.
    """

    # Ensure we have a Path object 
    path = Path(path)

    # Let pathlib handle the actual file reading because it gives good error messages
    content = path.read_text(encoding=encoding)

    # Create and return Document 
    return Document(path=path, content=content)

def load_document_with_metadata(
    path: Path,
    encoding: str = "utf-8", 
    include_stats: bool = False
) -> Document: 
    """Load a document and optionally include file statistics in metadata.

    This extends the basic loader with optional metadata collection. 
    Still not a forever contract. Just a convenience function. 

    Args: 
        path: Path to the file to load. 
        encoding: Text encoding to use (default: utf-8).
        include_stats: Whether to include file stats in metadata. 

    Returns: 
        A Document instance with content and optional metadata. 
    """

    # Load the basic document
    doc = load_document(path, encoding)

    # Optionally add file statistics to metadata 
    if include_stats: 
        stats = path.stat()
        doc.metadata["size_bytes"] = stats.st_size
        doc.metadata["modified_time"] = stats.st_mtime
        doc.metadata["created_time"] = stats.st_ctime
    
    return doc

