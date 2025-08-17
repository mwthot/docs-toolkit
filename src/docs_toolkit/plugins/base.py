"""Base Plugin class for docs-tookit.

This module defines the fundamenetal Plugin abstract base calss that
plugins must inherit from. This is a forever contract - all plugin
developers will depend on this interface. 
"""
from abc import ABC, abstractmethod 

from docs_toolkit.core.document import Document 

class Plugin(ABC): 
    """Abstract base class for all docs-toolkit plugins. 

    A Plugin processes a Document and returns a Document. This minimal
    interface is designed to be composable - plugins can be chained,
    run in parallel, or organized however users need. 

    The simplicity is intentional: no configuration in the interfaces,
    no lifecycle methods, no contex objects. Just process. 
    """

    @abstractmethod
    def process(self, document: Document) -> Document: 
        """Process a document and return the result. 

        This is the only method plugins must implement. The plugin
        can modify the document's content, update its metadata, or
        return an entirely new document. 

        Args: 
            document: The document to process. 

        Returns: 
            The processed document (can be the same modified instance
            or a new instance).
        """
        pass