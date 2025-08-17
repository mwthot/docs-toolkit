"""Tests for the Document model. Our forever contract.""" 
import pytest
from pathlib import Path 

from docs_toolkit.core.document import Document 

class TestDocument: 
    """Test the Document contract behaviors."""

    def test_minimal_documen_creation(self): 
        """Test creating a document with minimal required fiels."""
        doc = Document(
            path=Path("test.md"), 
            content="# Test Document"
        )
        assert doc.path == Path("test.md")
        assert doc.content == "# Test Document"
        assert doc.metadata == {}

    def test_document_with_metadata(self): 
        """Test that metadata dict is properly initialized."""
        metadata = {"author": "test", "version": "1.0"}
        doc = Document(
            path=Path("test.md"),
            content="content", 
            metadata=metadata
        )
        assert doc.metadata == metadata

    def test_metadata_default_is_mutable(self): 
        """Test that default metadata doesn't share state between istances."""
        doc1 = Document(path=Path("test1.md"), content="content1")
        doc2 = Document(path=Path("test2.md"), content="content2")

        doc1.metadata["key"] = "value1"
        doc2.metadata["key"] = "value2"

        assert doc1.metadata["key"] == "value1"
        assert doc2.metadata["key"] == "value2"

    def test_document_repr(self): 
        """Test readable representation for debugging."""
        doc = Document(
            path=Path("test.md"),
            content="x" * 100,
            metadata={"key": "value"}
        )
        repr_str = repr(doc)
        assert "test.md" in repr_str
        assert "100" in repr_str
        assert "key" in repr_str

    def test_document_str(self): 
        """Test string representation."""
        doc = Document(
            path=Path("example.md"),
            content="content"
        )
        str_repr = str(doc)
        assert "example.md" in str_repr