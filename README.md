# ssh-demo

Demo and [slides](slides.pdf) for my "Outgrowing Your Laptop With Positron" talk at `posit::conf(2025)`.

### To run the demo

Ensure [uv is installed](https://docs.astral.sh/uv/getting-started/installation/) and run `uv sync` in this repository to set up a virtual environment. Activate it with `source .venv/bin/activate`.

You can optionally pre-download all the parquet files with `python download.py`.

Then I'd recommend running the `analysis.py` file line-by-line with `Ctrl/Cmd + Enter` in Positron.

### Additional resources

Positron Remote SSH documentation: https://positron.posit.co/remote-ssh.html

Posit Workbench: https://posit.co/products/enterprise/workbench/

Ibis: https://ibis-project.org/
