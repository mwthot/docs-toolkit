#!/usr/bin/env python3
"""Simple runner to validate Phase 0 implementation.

This script demonstrates that our core contracts work together: 
- Loading a document 
- Applying a plugin 
- Outputting results 

This is intentionally simple. There is no CLI, no configuration, 
just validation that our abstractions compose correctly. 
"""

import sys
from pathlib import Path 

# Add src to Python path so we can import docs_toolkit
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rich.console import Console 
from rich.panel import Panel 
from rich.syntax import Syntax 

from docs_toolkit.core.document import Document 
from docs_toolkit.plugins.builtin.uppercase import UppercasePlugin

def main(): 
    """Run a simple transformation to validate our contracts."""
    console = Console()

    # Create a sample document 
    sample_content = """# Sample Document 

This is a test document to validate our plugin system. 
It contains multiple lines and demonstrates that our 
minimal contracts are sufficient for basic operations. 

## Features
- Simple document model 
- Minimal Plugin interface 
- Clear transformations
""" 

    # Create document instance
    doc = Document(
        path=Path("sample.md"),
        content=sample_content
    )

    # Display original 
    console.print(Panel(
        Syntax(doc.content, "markdown", theme="monokai"),
        title=f"[cyan]Original: {doc.path}[/cyan]",
        border_style="blue"
    ))

    # Apply plugin
    plugin = UppercasePlugin(preserve_original=True)
    result = plugin.process(doc)

    # Display transformed
    console.print(Panel(
        Syntax(result.content, "markdown", theme="monokai"),
        title=f"[green]Transformed: {result.path}[/green]",
        border_style="green"
    ))

    # Display metadata 
    console.print(Panel(
        f"[yellow]Metadata:[/yellow]\n"
        f"Character count: {result.metadata.get('character_count', 'N/A')}\n"
        f"Processing history: {len(result.metadata.get('processing_history', []))} plugin(s)\n"
        f"Original preserved: {('original_content' in result.metadata)}",
        title="[magenta]Document Metadata[/magenta]",
        border_style="magenta"
    ))

    console.print("[bold green]+[/bold green] Phase 0 validation complete!")
    console.print("Our minimal contracts successfully compose:")
    console.print(" * Document model holds data effectively")
    console.print(" * Plugin interface enables transformations")
    console.print(" * Metadata dict provides extensibility")

if __name__ == "__main__": 
    main()