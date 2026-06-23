import pathlib
import datetime

# The specific markdown files you want to combine (in this exact order)
target_files = [
    "market-analysis.md",
    "problem-brief.md",
    "validated-opportunity-brief.md",
    "stress-test-report.md"
]

datestring = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
output_file = f"report_{datestring}.md"

def find_file_anywhere(root, filename):
    """Search recursively for a file with the exact name."""
    for path in root.rglob(filename):
        if path.is_file():
            return path
    return None

def clear_file(path):
    """Set the file's content to empty."""
    path.write_text("", encoding="utf-8")

def combine_markdown_workspace(output_path):
    root_folder = pathlib.Path(".")
    filenames = target_files
    combined = []
    found_paths = []

    for name in filenames:
        found = find_file_anywhere(root_folder, name)
        if found:
            found_paths.append(found)
            combined.append(found.read_text(encoding="utf-8"))
            combined.append("\n\n")
        else:
            print(f"Warning: {name} not found anywhere under {root_folder}")

    # Write combined output
    pathlib.Path(output_path).write_text("".join(combined), encoding="utf-8")
    print(f"Combined {len(found_paths)} files into {output_path}")

    # Clear each source file
    for p in found_paths:
        clear_file(p)
        print(f"Cleared: {p}")

# Use the VS Code workspace root (".") as the search base
# workspace_root = pathlib.Path(".")

# combine_markdown_workspace(output_file)
