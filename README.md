# GCS Operations Agent

This project contains an agent designed to interact with Google Cloud Storage (GCS). It allows users to perform common GCS operations such as listing buckets, listing objects within a bucket, creating new buckets, and deleting objects from a bucket.

## Features

The agent provides the following functionalities:

-   **List Buckets**: Lists all GCS buckets in a specified project.
-   **List Objects**: Lists all objects within a specified GCS bucket.
-   **Create Bucket**: Creates a new GCS bucket in a specified project and location.
-   **Delete Object**: Deletes a specified object from a GCS bucket.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

-   **Python**: Version 3.8 or higher.
-   **Pip**: Python package installer.
-   **Google Cloud SDK (gcloud CLI)**: Installed and authenticated. You can authenticate by running:
    ```bash
    gcloud auth application-default login
    ```
-   **`google-adk` Python package**: This is the Agent Development Kit.
-   **Google Cloud Project**: Access to a Google Cloud Project with the Cloud Storage API enabled. The service account or credentials used will need appropriate permissions for GCS operations (e.g., `Storage Admin` or more granular roles like `Storage Object Admin`, `Storage Bucket Creator`).

## Setup

1.  **Clone the Repository (if applicable)**:
    If you haven't already, clone the repository to your local machine.
    ```bash
    # Example: git clone <repository-url>
    # cd <repository-name>  (e.g., cd ccd-hyderabad-adk)
    ```

2.  **Navigate to the Project Directory**:
    Change to the root directory of this ADK project (e.g., `/Users/sanketbisne/ccd-hyderabad-adk/`).
    ```bash
    cd /path/to/your/ccd-hyderabad-adk
    ```

3.  **Create and Activate Virtual Environment**:
    It's recommended to use a virtual environment. If `.venv` doesn't exist in the project root, create it:
    ```bash
    python3 -m venv .venv
    ```
    Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

4.  **Navigate to Agent Directory**:
    The agent code resides in the `ccd-ai-agent` subdirectory. Navigate into it:
    ```bash
    cd ccd-ai-agent
    ```

5.  **Install Dependencies**:
    Install the required Python packages using the `requirements.txt` file located in the `ccd-ai-agent` directory:
    ```bash
    pip install -r requirements.txt
    ```

## ADK Agent Commands

Ensure your virtual environment is active and you are in the `ccd-ai-agent` directory (`/Users/sanketbisne/ccd-hyderabad-adk/ccd-ai-agent/`) when running these commands.

### 1. Create the Agent

This command registers your agent definition with the ADK. The agent is defined as `root_agent` in the `agent.py` file.

```bash
adk create --agent_id gcs_operation_agent --agent_path agent:root_agent
```

-   `--agent_id gcs_operation_agent`: Specifies the unique ID for your agent.
-   `--agent_path agent:root_agent`: Points to the `root_agent` object within the `ccd-ai-agent/agent.py` module.

### 2. Deploy the Agent to Google Cloud Run

This command packages your agent and deploys it as a service on Google Cloud Run.

```bash
adk deploy gcs_operation_agent --platform=cloudrun --project <YOUR_PROJECT_ID> --region <YOUR_REGION>
```

-   `gcs_operation_agent`: The ID of the agent you created in the previous step.
-   `--platform=cloudrun`: Specifies Cloud Run as the deployment target.
-   `--project <YOUR_PROJECT_ID>`: Replace `<YOUR_PROJECT_ID>` with your Google Cloud Project ID.
-   `--region <YOUR_REGION>`: Replace `<YOUR_REGION>` with the Google Cloud region where you want to deploy the service (e.g., `us-central1`).

**Note on Permissions for Cloud Run:** The Cloud Run service will execute using a service account. Ensure this service account has the necessary IAM permissions to interact with Google Cloud Storage (e.g., roles like `roles/storage.objectAdmin`, `roles/storage.admin`, or custom roles with specific permissions like `storage.buckets.list`, `storage.buckets.create`, `storage.objects.list`, `storage.objects.delete`). By default, Cloud Run services use the Compute Engine default service account, but it's best practice to use a dedicated service account with least privilege.

## Interacting with the Deployed Agent

Once deployed, you can typically interact with your agent using the ADK CLI:
```bash
adk interact gcs_operation_agent
```
Follow the prompts to interact with your GCS operations agent.

## Project Structure

The main components of this project are organized as follows:

-   `.venv/`: Python virtual environment directory (should be in `.gitignore`).
-   `ccd-ai-agent/`: Directory containing the specific GCS agent code.
    -   `agent.py`: Contains the core logic for the GCS functions and the ADK agent definition.
    -   `requirements.txt`: Lists the Python dependencies specific to this agent.
    -   `__init__.py`: Makes the `ccd-ai-agent` directory a Python package.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
-   `README.md`: This file, providing an overview and instructions for the project.