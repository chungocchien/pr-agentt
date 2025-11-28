# PR Reviewer (`PRReviewer`)

## Overview

The `PRReviewer` class is responsible for reviewing pull requests and providing comprehensive feedback. It leverages AI models to analyze code changes, identify potential issues, and suggest improvements.

## Core Functionality

*   **Code Review**: Performs a detailed review of the pull request, assessing code quality, identifying bugs, and checking for security vulnerabilities.
*   **AI-Powered Feedback**: Utilizes AI models to generate review comments, suggestions, and summaries.
*   **Incremental Review**: Supports incremental reviews for pull requests with multiple commits, focusing on newly added or modified files.
*   **Configuration**: Allows customization of review criteria, such as requiring scores, tests, effort estimates, and security reviews.
*   **Ticket Compliance**: Integrates with ticket systems to ensure PRs comply with associated tickets.
*   **Labeling**: Automatically applies labels to pull requests based on review findings (e.g., review effort, security concerns).
*   **Auto-Approval**: Includes logic for automatic pull request approval based on predefined conditions.

## Key Methods

*   `run()`: Executes the pull request review process.
*   `_prepare_prediction()`: Gathers the PR diff and prepares it for AI analysis.
*   `_get_prediction()`: Interacts with the AI handler to obtain the review prediction.
*   `_prepare_pr_review()`: Processes the AI prediction and formats it into a markdown review.
*   `_get_user_answers()`: Retrieves user-provided answers from discussion messages for context.
*   `_can_run_incremental_review()`: Determines if an incremental review can be performed based on configuration and commit history.
*   `set_review_labels()`: Applies relevant labels to the pull request based on the review findings.

## Dependencies

*   `pr_agent.algo.ai_handlers.base_ai_handler.BaseAiHandler`
*   `pr_agent.algo.ai_handlers.openai_ai_handler.OpenAIHandler`
*   `pr_agent.algo.pr_processing`
*   `pr_agent.algo.token_handler.TokenHandler`
*   `pr_agent.algo.utils`
*   `pr_agent.config_loader.get_settings`
*   `pr_agent.git_providers`
*   `pr_agent.git_providers.git_provider.IncrementalPR`
*   `pr_agent.log.get_logger`
*   `pr_agent.servers.help.HelpMessage`
*   `pr_agent.tools.ticket_pr_compliance_check`

## Configuration

This component is configurable via `pr_reviewer` settings in the configuration file, including:

*   `require_score_review`
*   `require_tests_review`
*   `require_estimate_effort_to_review`
*   `require_can_be_split_review`
*   `require_security_review`
*   `extra_instructions`
*   `enable_help_text`
*   `persistent_comment`
*   `final_update_message`
*   `enable_custom_labels`
*   `enable_review_labels_effort`
*   `enable_review_labels_security`
*   `require_all_thresholds_for_incremental_review`
*   `minimal_commits_for_incremental_review`
*   `minimal_minutes_for_incremental_review`
*   `enable_auto_approval`
