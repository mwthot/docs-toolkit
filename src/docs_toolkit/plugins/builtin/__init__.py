"""Built-in plugins for docs-toolkit. 

These plugins demonstrate the plugin contract and provide 
immediately useful functionality without external dependencies. 
""" 
from docs_toolkit.plugins.builtin.uppercase import (
    UppercasePlugin, 
    UppercaseTitlePlugin,
)

__all__ = [
    'UppercasePlugin', 
    'UppercaseTitlePlugin',
]