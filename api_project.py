
import datetime
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator


def get_iss_location_and_save_to_file():
    url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    dt_object = datetime.datetime.fromtimestamp(
        timestamp, tz=datetime.timezone.utc
    )

    file_path = "/opt/airflow/dags/iss_positions.txt"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(
            f"{dt_object.isoformat()} | ISS | "
            f"Latitude: {latitude} | Longitude: {longitude}\n"
        )

    print(
        f"Successfully saved ISS location: "
        f"latitude={latitude}, longitude={longitude}"
    )


default_args = {
    "owner": "airflow",
    "start_date": datetime.datetime(2026, 10, 1),
}

with DAG(
    dag_id="iss_satellite_tracker",
    default_args=default_args,
    schedule="* * * * *",
    catchup=False,
) as dag:

    track_iss_task = PythonOperator(
        task_id="track_iss_location",
        python_callable=get_iss_location_and_save_to_file,
    )
