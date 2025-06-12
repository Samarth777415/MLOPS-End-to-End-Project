# promote_model.py (compatible with older MLflow versions)

import os
import mlflow

def promote_model():
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "gitesamarth"
    repo_name = "MLOPS-End-to-End-Project"

    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')
    client = mlflow.MlflowClient()

    model_name = "my_model"

    all_versions = client.search_model_versions(f"name='{model_name}'")

    staging_version = None
    prod_versions = []

    for v in all_versions:
        version_info = client.get_model_version(model_name, v.version)
        tags = version_info.tags  # Works in older versions of MLflow too

        if tags.get("stage") == "Staging":
            staging_version = v.version
        elif tags.get("stage") == "Production":
            prod_versions.append(v.version)

    if staging_version is None:
        raise ValueError("No model version tagged as 'Staging' found.")

    # Archive existing production versions
    for version in prod_versions:
        client.set_model_version_tag(model_name, version, "stage", "Archived")

    # Promote staging version to production
    client.set_model_version_tag(model_name, staging_version, "stage", "Production")
    print(f"Model version {staging_version} promoted to Production")

if __name__ == "__main__":
    promote_model()
