"""Uppercase plugin - Phase 0 proof of concept. 

This trivial plugin validates our core Plugin contract by implementing 
the simplest possible transformation: converting content to uppercase. 
While simple, it establishes patterns for error handling, documentation, 
and metadata updates that other plugins will follow. 
"""
from typing import Optional 

from docs_toolkit.core.document import Document 
from docs_toolkit.plugins.base import Plugin 

class UppercasePlugin(Plugin): 
    """Transform document content to uppercase. 
    
    This plugin serves as our Phase 0 proof of concept, validating that: 
    - The single-method plugin interface is sufficient 
    - Document transformation feels natural 
    - Metadata can be used to track processing 
    
    The implementation is intentionally trivial to focus on contract 
    validation rather than complex logic.
    """

    def __init__(self, preserve_original: bool = False): 
        """Initialize the UppercasePlugin. 

        Args: 
            preserve_original: If True, stores original content in metadata 
                                before transformation. Useful for debugging.  
        """
        self.preserve_original = preserve_original

    def process(self, document: Document) -> Document: 
        """Convert document content to uppercase. 

        Updates the document's metadata to track that this transformation
        was applied, demonstrating how plugins can communicate their 
        actions for downstream processing or debugging. 

        Args: 
            document: The document to transform. 

        Returns: 
            The same document instance with uppercase content. 

        Note: 
            This modified the document in-place and returns it, establishing
            a pattern where plugins can choose whether to mutate or create
            new instances based on their needs. 
        """
        # Store original if requested (demonstrates metadata usage)
        if self.preserve_original: 
            document.metadata['original_content'] = document.content

        # Perform the transformation
        document.content = document.content.upper()

        # Track that this plugin processed the document 
        # This demonstrates how plugins can add processing history
        if 'processing_history' not in document.metadata: 
            document.metadata['processing_history'] = []

        document.metadata['processing_history'].append({
            'plugin': 'UppercasePlugin', 
            'preserve_original': self.preserve_original,
        })

        # Update character count to demonstrate metadata updates
        document.metadata['character_count'] = len(document.content)

        return document



class UppercaseTitlePlugin(Plugin): 
    """Transform only the first line (title) to uppercase. 
    
    A slightly more sophisticated variant that demonstrates: 
    - Plugins can be composable (could chain with UppercasePlugin)
    - Different plugins can have different strategies
    - The same interface supports various transformations
    """

    def process(self, document: Document) -> Document: 
        """Convert the first line to uppercase, leave rest unchanged. 

        Args: 
            document: The document to transform. 

        Returns: 
            The document with its first line in uppercase. 
        """
        lines = document.content.splitlines(keepends=True)

        if lines: 
            # Transform first line only 
            lines[0] = lines[0].upper()
            document.content = "".join(lines)

            # Track this specific transformation
            if 'processing_history' not in document.metadata: 
                document.metadata['processing_history'] = []

            document.metadata['processing_history'].append({
                'plugin': 'UppercaseTitlePlugin',
                'lines_affected': 1, 
            })

        return document 