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

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PuzzledSkate/Taskology.git
   cd Taskology
   ```

2. **Set Up Environment Variables:**
   Create a .env file in the project root with the following content:
   ```DATABASE_URL=postgresql://postgres:postgres@db:5432/todo_db
   ```

3. **Run the Applicationn with Docker Compose:**
   ```docker-compose up --build
   ```

4. **Access the API:**
- `http://127.0.0.1:5000`
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




