# h5manager/cli.py
import pathlib, typer
from . import converter, merger, visualizer, config

app = typer.Typer(add_completion=False)

@app.command()
def convert(
    input_dir: pathlib.Path,
    output: pathlib.Path = typer.Option(..., help="Output .h5 file (no suffix)"),
    dim: int = typer.Option(config.get("image_dim"), help="Target square dimension (px)"),
):
    typer.echo(f"Converting {input_dir} → {output.with_suffix('.h5')} (dim={dim})")
    converter.convert_dir(input_dir, output, dim)

@app.command()
def merge(
    inputs: str = typer.Option(..., help="Comma‑separated file list or glob"),
    output: pathlib.Path = typer.Option(..., help="Merged .h5 output (no suffix)"),
):
    typer.echo(f"Merging {inputs} → {output.with_suffix('.h5')}")
    merger.merge(inputs, output)

@app.command()
def visualize(file: pathlib.Path):
    typer.echo(f"Visualizing {file}")
    visualizer.visualize(file)
