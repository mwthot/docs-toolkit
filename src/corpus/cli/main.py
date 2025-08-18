import click 
from pathlib import Path 
from rich.console import console

console = Console()

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--format', type=click.Choice(['console', 'html', 'json']), default='console')
@click.option('--horror-level', type=click.IntRange(1,5), default=2)
def examine(directory, format, horror_level): 
    """Examine documentation corpus for pathologies.""""

    console.print("\n[bold red] EXAMINING CORPUS:[/bold red]", Path(directory).absolute())
    console.print()

    # For now, just list markdown files to verify it works 
    docs = list(Path(directory).glob("**/*.md"))
    console.print(f"Found {len(docs)} cells to examine...")

    for doc in docs[:5]: # Just show first 5 for now 
        console.print(f"  - {doc.name}")

if __name__ == '__main__': 
    examine()