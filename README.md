
# Connect a Python application on Cloud Run to a Cloud SQL for PostgreSQL database

Using [Cloud SQL Python connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/tree/main) to securely connect your Python application to your Cloud SQL database. 

This repository will demonstrate how to connect a Python application on Cloud Run to a Cloud SQL for PostgreSQL database securely with a service account using IAM Authentication.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`INSTANCE_CONNECTION_NAME` = "{PROJECT_ID}:{REGION}:{INSTANCE_NAME}"

`DB_USER` = "sql-client-service-account@{PROJECT_ID}.iam"

`DB_PASS` = (optional, if followed the `cloudsql.iam_authentication`)

`PRIVATE_IP` = (conditional) if true it will use PRIVATE_IP is not set it will use PUBLIC_IP to connect to Cloud SQL

`DB_NAME` = your-database


## Supported Articles

[Connect a Python application on Cloud Run to a Cloud SQL for PostgreSQL database](https://medium.com/@kellenjohn175/how-to-guides-gcp-cloudsql-iam-%E8%BA%AB%E4%BB%BD%E9%A9%97%E8%AD%89%E6%95%B4%E5%90%88%E4%B8%A6%E4%BD%BF%E7%94%A8-cloud-sql-connector-%E8%A8%AA%E5%95%8F%E8%B3%87%E6%96%99%E5%BA%AB-python-24b502e9bfd4)

