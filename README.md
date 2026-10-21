# ISS Tracker Airflow Pipeline 🚀

A containerized Apache Airflow pipeline that automatically fetches, tracks, and logs the real-time geographic coordinates of the International Space Station (ISS).

*   • Created an Airflow DAG (api_project.py) to automatically fetch real-time ISS coordinates.
• Configured Docker Compose (docker-compose.yaml) to easily launch Airflow along with a Postgres database backend.
• Ran the environment using docker compose down && docker compose up -d directly inside VS Code.
• Successfully logged data including the exact timestamp, latitude, and longitude into iss_positions.txt.# Real-Time-ISS-Tracker-
 Successfully logged data including the exact timestamp, latitude, and longitude into iss_positions.txt.


## 📂 Project Structure

*   **`dags/api_project.py`** - Core Airflow DAG script defining the task logic, API request scheduling, and logging mechanisms.
*   **`docker-compose.yaml`** - Multi-container orchestration config for running the Airflow Webserver, Scheduler, and PostgreSQL database.
*   **`Dockerfile`** - Custom container image configuration for installing required system and Python dependencies.
*   **`dags/iss_positions.txt`** - Automated output log tracking raw spatial data (`Timestamp | ISS | Latitude | Longitude`).
*
