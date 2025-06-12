--- /dev/null
+++ b/Users/sanketbisne/ccd-hyderabad-adk/ccd-ai-agent/README.md
@@ -0,0 +1,110 @@
+# GCS Operations Agent
+
+This agent is designed to interact with Google Cloud Storage (GCS). It allows users to perform common GCS operations such as listing buckets, listing objects within a bucket, creating new buckets, and deleting objects from a bucket.
+
+## Features
+
+The agent provides the following functionalities:
+
+-   **List Buckets**: Lists all GCS buckets in a specified project.
+-   **List Objects**: Lists all objects within a specified GCS bucket.
+-   **Create Bucket**: Creates a new GCS bucket in a specified project and location.
+-   **Delete Object**: Deletes a specified object from a GCS bucket.
+
+## Prerequisites
+
+Before you begin, ensure you have the following installed and configured:
+
+-   **Python**: Version 3.8 or higher.
+-   **Pip**: Python package installer.
+-   **Google Cloud SDK (gcloud CLI)**: Installed and authenticated. You can authenticate by running:
+    ```bash
+    gcloud auth application-default login
+    ```
+-   **`google-adk` Python package**: This is the Agent Development Kit.
+-   **Google Cloud Project**: Access to a Google Cloud Project with the Cloud Storage API enabled. The service account or credentials used will need appropriate permissions for GCS operations (e.g., `Storage Admin` or more granular roles like `Storage Object Admin`, `Storage Bucket Creator`).
+
+## Setup
+
+1.  **Clone the Repository (if applicable)**:
+    If this agent is part of a larger repository, clone it to your local machine.
+    ```bash
+    # Example: git clone <repository-url>
+    # cd <repository-name>
+    ```
+
+2.  **Navigate to the Project Directory**:
+    Change to the root directory of this ADK project. Based on your context, this is likely `/Users/sanketbisne/ccd-hyderabad-adk/`.
+    ```bash
+    cd /Users/sanketbisne/ccd-hyderabad-adk/
+    ```
+
+3.  **Activate Virtual Environment**:
+    Your project uses a virtual environment located at `.venv`. Activate it:
+    ```bash
+    source .venv/bin/activate
+    ```
+    If the virtual environment doesn't exist, you might need to create it first (e.g., `python3 -m venv .venv`) from the `/Users/sanketbisne/ccd-hyderabad-adk/` directory.
+
+4.  **Navigate to Agent Directory**:
+    Change to the agent's specific directory:
+    ```bash
+    cd ccd-ai-agent
+    ```
+
+5.  **Install Dependencies**:
+    Install the required Python packages using the `requirements.txt` file located in this directory:
+    ```bash
+    pip install -r requirements.txt
+    ```
+
+## ADK Agent Commands
+
+Ensure your virtual environment is active and you are in the `ccd-ai-agent` directory (`/Users/sanketbisne/ccd-hyderabad-adk/ccd-ai-agent/`) when running these commands.
+
+### 1. Create the Agent
+
+This command registers your agent definition with the ADK. The agent is defined as `root_agent` in the `agent.py` file.
+
+```bash
+adk create --agent_id gcs_operation_agent --agent_path agent:root_agent
+```
+
+-   `--agent_id gcs_operation_agent`: Specifies the unique ID for your agent.
+-   `--agent_path agent:root_agent`: Points to the `root_agent` object within your `agent.py` module.
+
+### 2. Deploy the Agent to Google Cloud Run
+
+This command packages your agent and deploys it as a service on Google Cloud Run.
+
+```bash
+adk deploy gcs_operation_agent --platform=cloudrun --project <YOUR_PROJECT_ID> --region <YOUR_REGION>
+```
+
+-   `gcs_operation_agent`: The ID of the agent you created in the previous step.
+-   `--platform=cloudrun`: Specifies Cloud Run as the deployment target.
+-   `--project <YOUR_PROJECT_ID>`: Replace `<YOUR_PROJECT_ID>` with your Google Cloud Project ID.
+-   `--region <YOUR_REGION>`: Replace `<YOUR_REGION>` with the Google Cloud region where you want to deploy the service (e.g., `us-central1`).
+
+**Note on Permissions for Cloud Run:** The Cloud Run service will execute using a service account. Ensure this service account has the necessary IAM permissions to interact with Google Cloud Storage (e.g., roles like `roles/storage.objectAdmin`, `roles/storage.admin`, or custom roles with specific permissions like `storage.buckets.list`, `storage.buckets.create`, `storage.objects.list`, `storage.objects.delete`). By default, Cloud Run services use the Compute Engine default service account, but it's best practice to use a dedicated service account with least privilege.
+
+## Interacting with the Deployed Agent
+
+Once deployed, you can typically interact with your agent using the ADK CLI or by making direct HTTP requests to the Cloud Run service endpoint if the ADK exposes it that way.
+
+For example, using the ADK CLI:
+```bash
+adk interact gcs_operation_agent
+```
+Follow the prompts to interact with your GCS operations agent.
+
+## Agent Code Structure
+
+-   `agent.py`: Contains the core logic for the GCS functions and the agent definition.
+-   `requirements.txt`: Lists the Python dependencies for the agent.
+-   `__init__.py`: Makes the `ccd-ai-agent` directory a Python package.
+
+```

This README provides a comprehensive guide for setting up, creating, and deploying your GCS agent using the ADK. Remember to replace placeholders like `<YOUR_PROJECT_ID>` and `<YOUR_REGION>` with your actual project details.
