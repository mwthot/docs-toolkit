"""Tests for the document loader functionality."""
import pytest 
from pathlib import Path 

from docs_toolkit.core.document import Document 
from docs_toolkit.core.loader import load_document, load_document_with_metadata

class TestDocumentLoader: 
    """Test document loading functionality."""

    def test_load_simple_document(self, tmp_path): 
        """Test loading a basic text file."""
        # Create a test file 
        test_file = tmp_path / "test.md"
        test_content = "# Test Document\n\nThis is content."
        test_file.write_text(test_content)

        # Load it 
        doc = load_document(test_file)

        assert isinstance(doc, Document)
        assert doc.path == test_file
        assert doc.content == test_content 
        assert doc.metadata == {}

    def test_load_nonexistent_file(self): 
        """Test that loading nonexistent file raises appropriate error."""
        with pytest.raises(FileNotFoundError): 
            load_document(Path("nonexistent.md"))

    def test_load_document_with_metadata(self, tmp_path): 
        """Test loading document with file statistics."""
        test_file = tmp_path / "test.md"
        test_content = "# Test"
        test_file.write_text(test_content)

        doc = load_document_with_metadata(test_file, include_stats=True)

        assert isinstance(doc, Document)
        assert doc.content == test_content 
        assert "size_bytes" in doc.metadata 
        assert "modified_time" in doc.metadata 
        assert "created_time" in doc.metadata