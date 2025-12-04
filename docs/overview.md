# PR-Agent Repository Overview

The `pr-agent` repository provides an automated tool that enhances the pull request (PR) review process. It leverages AI to provide insights, suggestions, and automation for various PR-related tasks, such as code review, description generation, and labeling.

## Architecture

The `pr-agent` architecture is designed to be modular and extensible. The core component is the `PRAgent` class, which acts as the central command processing unit. It receives user requests, parses them, dispatches them to the appropriate tools, and orchestrates the overall workflow. The tools then interact with AI handlers and Git providers to perform their specific tasks.

```mermaid
graph TD
    A[User Request] --> B{PRAgent.handle_request};
    B --> C{Apply Repo Settings};
    B --> D{Parse Request & Args};
    B --> E{Validate & Update Settings};
    B --> F{Determine Command};
    F -- "Command Map (command2class)" --> G{Instantiate Tool};
    G -- "e.g., PRReviewer, PRDescription" --> H[Execute Tool.run() ];
    H --> I[AI Handler];
    H --> J[Git Provider];
    H --> K[Logging];
    I --> L[AI Model];
    J --> M[Git Repository];
    H --> N[Response to User];

    subgraph Core Agent
        B
        C
        D
        E
        F
        G
        H
    end

    subgraph AI Handlers
        I
        L
    end

    subgraph Git Providers
        J
        M
    end

    subgraph Tools
        G
    end

    subgraph Utilities & Logging
        K
    end
```

## Core Modules

The repository is structured into several core modules:

-   **`core_agent`**: The central command processing unit, responsible for receiving user requests, parsing them, dispatching them to the appropriate tools, and orchestrating the overall workflow. See [core_agent documentation](pr_agent/agent/core_agent.md).
-   **`ai_handlers`**: Provides a standardized interface and various implementations for interacting with different AI models. See [ai_handlers documentation](pr_agent/algo/ai_handlers/ai_handlers.md).
-   **`git_providers`**: Provides an abstraction layer for interacting with various Git providers (e.g., GitHub, GitLab, Azure DevOps, Bitbucket, CodeCommit). See [git_providers documentation](pr_agent/git_providers/git_providers.md).
-   **`tools`**: Provides a collection of classes, each implementing a specific action or tool that the PR-Agent can perform on a pull request. See [tools documentation](pr_agent/tools/tools.md).
-   **`utilities_and_types`**: Contains utility classes, data structures, and type definitions used throughout the PR-Agent application. See [utilities_and_types documentation](pr_agent/algo/utilities_and_types.md).
-   **`identity_providers`**: Responsible for determining the eligibility of a Git provider to use the PR-Agent tool. See [identity_providers documentation](pr_agent/identity_providers/identity_providers.md).
-   **`secret_providers`**: Responsible for securely managing and retrieving secrets used by the PR-Agent. See [secret_providers documentation](pr_agent/secret_providers/secret_providers.md).
-   **`logging`**: Handles logging functionality for the PR-Agent.

## Module Dependencies

The modules within the `pr-agent` repository have the following key dependencies:

-   `core_agent` depends on `ai_handlers`, `git_providers`, `tools`, `utilities_and_types`, and `logging`.
-   `ai_handlers` depends on `utilities_and_types`.
-   `git_providers` depends on `utilities_and_types`.
-   `tools` depends on `ai_handlers`, `git_providers`, and `utilities_and_types`.
-   `identity_providers` depends on `git_providers`.
-   `secret_providers` is used by `ai_handlers` and `config_loader`.

This modular design allows for easy extension and customization of the PR-Agent's functionality.