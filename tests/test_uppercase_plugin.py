"""Tests for the UppercasePlugin - validating our plugin contract.""" 
import pytest 
from pathlib import Path 

from docs_toolkit.core.document import Document 
from docs_toolkit.plugins.builtin.uppercase import (
    UppercasePlugin, 
    UppercaseTitlePlugin,
)

class TestUppercasePlugin: 
    """Test the UppercasePlugin proof of concept."""

    def test_basic_transformation(self): 
        """Test that content is transformed to uppercase."""
        doc = Document(
            path=Path("test.md"),
            content="hello world\nthis is a test"
        )
        plugin = UppercasePlugin()
        result = plugin.process(doc)

        # verify in-place modification pattern 
        assert result is doc
        assert result.content == "HELLO WORLD\nTHIS IS A TEST"

    def test_empty_document(self): 
        """Test handling of empty content."""
        doc = Document(path=Path("empty.md"), content="")
        plugin = UppercasePlugin()
        result = plugin.process(doc)

        assert result.content == ""
        assert 'character_count' in result.metadata
        assert result.metadata['character_count'] == 0

    def test_preserve_original_option(self): 
        """Test that preserve_original stores original content."""
        original_content = "Mixed Case Content" 
        doc = Document(
            path=Path("test.md"),
            content = original_content
        )

        plugin = UppercasePlugin(preserve_original=True)
        result = plugin.process(doc)

        assert result.content == "MIXED CASE CONTENT" 
        assert result.metadata['original_content'] == original_content

    def test_processing_history_tracking(self): 
        """Test that plugin tracks its processing in metadata.""" 
        doc = Document(path=Path("test.md"), content="test")
        plugin = UppercasePlugin()

        result = plugin.process(doc)

        assert 'processing_history' in result.metadata 
        assert len(result.metadata['processing_history']) == 1

        history = result.metadata['processing_history'][0]
        assert history['plugin'] == 'UppercasePlugin'
        assert 'preserve_original' in history 

    def test_multiple_plugin_applications(self): 
        """Test that processing history accumulates."""
        doc = Document(path=Path("test.md"), content="test")

        plugin1 = UppercasePlugin()
        plugin2 = UppercasePlugin(preserve_original=True)

        plugin1.process(doc)
        plugin2.process(doc)

        assert len(doc.metadata['processing_history']) == 2
        assert doc.metadata['processing_history'][0]['preserve_original'] is False
        assert doc.metadata['processing_history'][1]['preserve_original'] is True

    def test_unicode_content(self): 
        """Test handling of unicode characters."""
        doc = Document(
            path=Path("unicode.md"),
            content="Héllo Wörld 你好 🚀"
        )
        plugin = UppercasePlugin()
        result = plugin.process(doc)

        assert result.content == "HÉLLO WÖRLD 你好 🚀"

class TestUppercaseTitlePlugin: 
    """Test the UppercaseTitlePlugin variant."""

    def test_tile_only_transformation(self): 
        """Test that only first line is transformed."""
        doc = Document(
            path=Path("test.md"),
            content="# title here\nbody content\nmore content"
        )
        plugin = UppercaseTitlePlugin()
        result = plugin.process(doc)

        assert result.content == "# TITLE HERE\nbody content\nmore content"

    def test_single_line_document(self): 
        """Test document with only one line."""
        doc = Document(
            path=Path("single.md"),
            content="only line"
        )
        plugin = UppercaseTitlePlugin()
        result = plugin.process(doc)

        assert result.content == "ONLY LINE"

    def test_empty_document_handling(self): 
        """Test that empty documents are handled gracefully."""
        doc = Document(path=Path("empty.md"), content="")
        plugin = UppercaseTitlePlugin()
        result = plugin.process(doc)

        assert result.content == ""
        # Should not crash, but might not add history for empty doc

    def test_composability_with_base_plugin(self): 
        """Test that plugins can be chained together."""
        doc = Document(
            path=Path("test.md"),
            content="# Title\nbody text"
        )

        # Apply title plugin first 
        title_plugin = UppercaseTitlePlugin()
        title_plugin.process(doc)

        assert doc.content == "# TITLE\nbody text"

        # Then apply full uppercase
        full_plugin = UppercasePlugin()
        full_plugin.process(doc)

        assert doc.content == "# TITLE\nBODY TEXT"

        # Check both plugins recorded their work 
        assert len(doc.metadata['processing_history']) == 2
        assert doc.metadata['processing_history'][0]['plugin'] == 'UppercaseTitlePlugin'
        assert doc.metadata['processing_history'][1]['plugin'] == 'UppercasePlugin'