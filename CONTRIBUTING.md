# Contributing to gimi9_tree_view

First off, thank you for considering contributing to gimi9_tree_view! It's people like you that make this project great.

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by opening an issue on our [GitHub repository](https://github.com/gisman/tree-view/issues). Please include as much detail as possible, including steps to reproduce the bug, your environment, and any relevant logs or screenshots.

### Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing feature, please open an issue on our [GitHub repository](https://github.com/gisman/tree-view/issues). Describe your idea in detail and explain why you think it would be a good addition to the project.

### Submitting Pull Requests

1. **Fork the repository**: Click the "Fork" button on the top right of the repository page to create a copy of the repository on your GitHub account.

2. **Clone your fork**: Clone your forked repository to your local machine.
    ```bash
    git clone https://github.com/your-username/tree-view.git
    cd tree-view
    ```

3. **Create a new branch**: Create a new branch for your work.
    ```bash
    git checkout -b my-feature-branch
    ```

4. **Make your changes**: Make your changes to the codebase. Be sure to follow the project's coding style and conventions.

5. **Run tests**: Ensure that all tests pass and add new tests if necessary.
    ```bash
    pytest tests
    ```

6. **Commit your changes**: Commit your changes with a descriptive commit message.
    ```bash
    git add .
    git commit -m "Description of my changes"
    ```

7. **Push to your fork**: Push your changes to your forked repository.
    ```bash
    git push origin my-feature-branch
    ```

8. **Open a pull request**: Go to the original repository and open a pull request. Provide a clear and descriptive title and description for your pull request.

### Code Style

Please follow the PEP 8 style guide for Python code. You can use tools like `flake8` to check your code for style issues.

### Running Tests

We use `pytest` for testing. To run the tests, simply run:
```bash
pytest tests
```