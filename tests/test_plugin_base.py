"""Tests for the Plugin base contract."""
import pytest 
from pathlib import Path 

from docs_toolkit.core.document import Document 
from docs_toolkit.plugins.base import Plugin 

class TestPluginContract: 
    """Test the Plugin abstract base class contract."""

    def test_cannot_instantiate_abstract_plugin(self): 
        """Test that Plugin ABC cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Can't instantiate abstract class"): 
            Plugin()

    def test_plugin_requires_process_method(self): 
        """Test that plugins must implement process method."""
        # Try to create a plugin without a process method
        class IncompletePlugin(Plugin): 
            pass 

        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            IncompletePlugin()

    def test_valid_plugin_implementation(self): 
        """Test that a properly implemeneted plugin works."""
        class NoOpPlugin(Plugin): 
            def process(self, document: Document) -> Document: 
                return document 

        # Should instantiate without error 
        plugin = NoOpPlugin()

        # Should process a document
        doc = Document(path=Path("test.md"), content="test")
        result = plugin.process(doc)
        assert result is doc