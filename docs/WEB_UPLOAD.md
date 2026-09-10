# Browser-only GitHub update guide

GitHub's normal web interface stores ZIP files as ZIP files; uploading a ZIP to the repository root does **not** unpack it into the repository.

For a browser-only workflow, use one of these approaches:

1. Download and extract the provided ZIP with the operating system's built-in archive support, then open GitHub → **Add file → Upload files** and drag the extracted files/folders into the repository. No Git CLI or development tools are required.
2. Alternatively, ask ChatGPT to apply the prepared v2.0 files directly to a GitHub branch through the connected GitHub integration, then review/merge the branch in the browser.

When replacing v1, overwrite the same top-level filenames. The new `.gitignore` prevents future notebook checkpoint files from being added, but an already tracked `.ipynb_checkpoints` directory must be deleted separately if you want it removed from the repository history/current tree.
