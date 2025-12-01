# Utilities and Types Module

This module provides essential utility functions and data types for the PR-Agent.

## Overview

The `utilities_and_types` module is a foundational part of the PR-Agent, offering a collection of tools and data structures that are used across various functionalities. It includes components for handling command-line arguments, managing tokens, defining file edit types, and representing various data structures related to pull requests and code reviews.

## Architecture

This module is designed with a focus on reusability and modularity. It comprises several sub-modules, each responsible for a specific set of utilities or types.

### Core Components

*   **`CliArgs`**: Handles the validation of user-provided command-line arguments, ensuring that forbidden arguments are not used.
*   **`TokenHandler` and `TokenEncoder`**: Manages tokenization for language models, including encoding strings and counting tokens, with support for different models and accurate estimation.
*   **`EDIT_TYPE` and `FilePatchInfo`**: Defines an enumeration for different types of file edits and a data class to store detailed information about file patches.
*   **Utility Functions**: Includes various helper functions for tasks such as:
    *   Determining model types (`ModelType`)
    *   Formatting PR review headers (`PRReviewHeader`)
    *   Managing reasoning effort (`ReasoningEffort`)
    *   Handling PR description headers (`PRDescriptionHeader`)
    *   Parsing and formatting data for markdown output.
    *   Managing rate limits for GitHub API.
    *   Utility functions for loading and parsing configuration files (YAML).

## Sub-modules

This module is further organized into the following sub-modules:

*   [CLI Arguments](cli_args.md)
*   [Token Handling](token_handler.md)
*   [Types](types.md)
*   [Utilities](utils.md)
