# CodeCommit Provider and Client Module Documentation

This module provides integration with AWS CodeCommit as a Git provider for the PR-Agent. It includes classes for interacting with CodeCommit repositories, handling pull requests, and managing file differences.

## Architecture

The module consists of two main parts:

1.  **CodeCommitProvider**: Implements the `GitProvider` interface to provide a consistent way to interact with CodeCommit repositories.
2.  **CodeCommitClient**: A client that uses the AWS boto3 SDK to interact with the AWS CodeCommit service.

```mermaid
classDiagram
    GitProvider <|-- CodeCommitProvider
    CodeCommitProvider -- CodeCommitClient
    CodeCommitProvider -- CodeCommitFile
    CodeCommitProvider -- PullRequestCCMimic
    CodeCommitClient -- CodeCommitPullRequestResponse
    CodeCommitClient -- CodeCommitDifferencesResponse
    CodeCommitPullRequestResponse -- CodeCommitPullRequestTarget

    class GitProvider {
        <<interface>>
        +get_files()
        +get_diff_files()
        +publish_description()
        +publish_comment()
        +publish_code_suggestions()
        +...
    }
    class CodeCommitProvider {
        +set_pr(pr_url: str)
        +get_files() : list[CodeCommitFile]
        +get_diff_files() : list[FilePatchInfo]
        +publish_description(pr_title: str, pr_body: str)
        +publish_comment(pr_comment: str, is_temporary: bool = False)
        +publish_code_suggestions(code_suggestions: list) -> bool
        +...
    }
    class CodeCommitClient {
        +get_differences(repo_name: str, destination_commit: str, source_commit: str)
        +get_file(repo_name: str, file_path: str, sha_hash: str, optional: bool = False)
        +get_pr(repo_name: str, pr_number: int)
        +publish_description(pr_number: int, pr_title: str, pr_body: str)
        +publish_comment(repo_name: str, pr_number: int, destination_commit: str, source_commit: str, comment: str, annotation_file: str = None, annotation_line: int = None)
        +...
    }
    class CodeCommitFile {
        +a_path: str
        +a_blob_id: str
        +b_path: str
        +b_blob_id: str
        +edit_type: EDIT_TYPE
        +filename: str
    }
    class PullRequestCCMimic {
        +title: str
        +diff_files: List[FilePatchInfo]
        +description: str
        +source_commit: str
        +source_branch: str
        +destination_commit: str
        +destination_branch: str
    }
    class CodeCommitPullRequestResponse {
        +title: str
        +description: str
        +targets: list[CodeCommitPullRequestTarget]
    }
    class CodeCommitPullRequestTarget {
        +source_commit: str
        +source_branch: str
        +destination_commit: str
        +destination_branch: str
    }
    class CodeCommitDifferencesResponse {
        +before_blob_id: str
        +before_blob_path: str
        +after_blob_id: str
        +after_blob_path: str
        +change_type: str
    }
```

## Functionality

### 1. CodeCommitProvider

This class is the main entry point for interacting with CodeCommit repositories. It implements the `GitProvider` interface (defined in [git_provider_base.md](git_provider_base.md)) and provides methods for:

*   Setting up the connection to a pull request using its URL.
*   Retrieving file information and diffs.
*   Publishing descriptions, comments, and code suggestions to a pull request.
*   Fetching the list of languages used in the pull request.

See [CodeCommitProvider Detailed Documentation](CodeCommitProvider Detailed Documentation.md) for more details.

### 2. CodeCommitClient

This class is a client for interacting with the AWS CodeCommit service using the boto3 SDK. It provides methods for:

*   Connecting to the AWS CodeCommit service.
*   Retrieving file differences between two commits.
*   Retrieving file content.
*   Retrieving pull request information.
*   Publishing descriptions and comments to a pull request.

See [CodeCommitClient Detailed Documentation](CodeCommitClient Detailed Documentation.md) for more details.
