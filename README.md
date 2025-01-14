# To-Do Application

This project is a secure and scalable To-Do application built with Python Flask, PostgreSQL, and Docker. It provides a RESTful API for managing tasks and is containerized for portability. The application will be expanded with a frontend and deployed to Google Cloud in subsequent phases.

---

## Features

- RESTful API with CRUD operations for tasks.
- PostgreSQL database integration.
- `/health` endpoint for monitoring.
- Dockerized for consistent deployment across environments.
- Modular and extensible architecture.

---

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python 3.12+
- PostgreSQL
- Docker (optional, for containerized setup)
- Git

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the project root with the following content:
   ```env
   DATABASE_URL=postgresql://<username>:<password>@localhost:5432/todo_db
   ```
   Replace `<username>` and `<password>` with your PostgreSQL credentials.

5. **Initialize the Database:**
   - Start your PostgreSQL server.
   - Create the database:
     ```sql
     CREATE DATABASE todo_db;
     ```
   - Run the application to create the tables:
     ```bash
     flask run
     ```

6. **Run the Application:**
   ```bash
   flask run
   ```
   Access the API at `http://127.0.0.1:5000`.

---

## API Endpoints

| Endpoint          | Method | Description            |
|-------------------|--------|------------------------|
| `/todos`          | GET    | Fetch all tasks.       |
| `/todos`          | POST   | Create a new task.     |
| `/todos/<id>`     | PUT    | Update an existing task. |
| `/todos/<id>`     | DELETE | Delete a task.         |
| `/health`         | GET    | Check API health.      |

---

## Running with Docker

1. **Build the Docker Image:**
   ```bash
   docker build -t todo-api .
   ```

2. **Run the Container:**
   ```bash
   docker run -d -p 5000:5000 --name todo-api-container todo-api
   ```

3. **Access the API:**
   Visit `http://127.0.0.1:5000`.

4. **Stop the Container:**
   ```bash
   docker stop todo-api-container
   docker rm todo-api-container
   ```

---

## Testing

1. **Run Unit Tests:**
   ```bash
   pytest tests/
   ```

2. **Check API Functionality:**
   Use a tool like [Postman](https://www.postman.com/) or `curl` to test endpoints.

---

## Roadmap

### Current Progress:
- [x] Develop basic API with CRUD functionality.
- [x] Integrate PostgreSQL.
- [x] Dockerize the application.

### Upcoming Tasks:
- [ ] Set up CI/CD pipelines.
- [ ] Deploy to Google Cloud Run.
- [ ] Add a secure frontend for user interaction.
- [ ] Implement monitoring and logging.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- Flask and its community.
- PostgreSQL for robust database support.
- Docker for simplifying deployment.

---

## Contact




