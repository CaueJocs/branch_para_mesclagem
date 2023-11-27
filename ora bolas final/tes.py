import nbformat
import sys

def merge_notebooks(notebook_paths, output_path):
    merged_notebook = nbformat.v4.new_notebook()

    for path in notebook_paths:
        with open(path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        merged_notebook.cells.extend(notebook.cells)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        nbformat.write(merged_notebook, output_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python merge_notebooks.py arquivo1.ipynb arquivo2.ipynb ... saida.ipynb")
        sys.exit(1)

    notebook_paths = sys.argv[1:-1]
    output_path = sys.argv[-1]

    merge_notebooks(notebook_paths, output_path)


