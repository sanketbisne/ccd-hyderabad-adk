
from google.cloud import storage
from google.adk.agents import Agent


# ---------------------------------------------
# GCS Functions ()
# ---------------------------------------------

def list_buckets(project_id: str) -> dict:
    """Lists all GCS buckets in the project."""
    try:
        storage_client = storage.Client(project=project_id)
        buckets = list(storage_client.list_buckets())
        bucket_names = [bucket.name for bucket in buckets]
        return {"status": "success", "buckets": bucket_names}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


def list_objects(bucket_name: str) -> dict:
    """Lists all objects in a GCS bucket."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs()
        object_names = [blob.name for blob in blobs]
        return {"status": "success", "objects": object_names}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


def delete_object(bucket_name: str, blob_name: str) -> dict:
    """Deletes an object from a GCS bucket."""
    try:
        print(f"Deleting blob: {blob_name} from bucket: {bucket_name}")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()
        print("Delete successful.")
        return {
            "status": "success",
            "message": f"Blob {blob_name} deleted from bucket {bucket_name}.",
        }
    except Exception as e:
        print(f"Delete failed: {str(e)}")
        return {"status": "error", "error_message": str(e)}


def create_bucket(project_id: str, bucket_name: str, location: str = "US") -> dict:
    """Creates a new GCS bucket."""
    try:
        print(f"Creating bucket: {bucket_name} in project: {project_id} at location: {location}")
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.bucket(bucket_name)
        new_bucket = storage_client.create_bucket(bucket, location=location)
        print("Bucket created successfully.")
        return {
            "status": "success",
            "message": f"Bucket {new_bucket.name} created in location {new_bucket.location}.",
        }
    except Exception as e:
        print(f"Bucket creation failed: {str(e)}")
        return {"status": "error", "error_message": str(e)}


    
# ---------------------------------------------
#  Our Root Agent
# ---------------------------------------------

root_agent = Agent(
    name="gcs_operation_agent",
    model="gemini-2.0-flash",
    description="An agent that interacts with Google Cloud Storage (GCS). It can list buckets, "
                "list objects within a bucket, create new buckets, and delete objects from a bucket.",
    instruction=(
        "You are a helpful assistant for managing Google Cloud Storage. You can perform operations "
        "such as creating buckets, listing existing buckets, listing objects in a bucket, and deleting specific objects."
    ),
    tools=[
        list_buckets,
        list_objects,
        delete_object,
        create_bucket,
    ],
)
