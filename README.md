# README

CI/CD Pipeline with Jenkins, Docker, and a Python Flask API This repository contains all the source code for the project built in the first video of the Tech with JP YouTube channel.

📺 **Watch the full tutorial on YouTube!** This project is a code-along tutorial. You can follow all the steps from scratch by watching the video:

[CODE ALONG] Building a CI/CD Pipeline with Jenkins and Docker https://youtu.be/M3TC5uY0m00?feature=shared

📋 **About The Project** The goal of this project is to build a complete, automated CI/CD (Continuous Integration/Continuous Delivery) pipeline from the ground up.

We start by creating a simple web API using Python and the Flask framework. We then package this application into a portable, consistent environment using Docker. Finally, we configure a Jenkins server to automatically watch our GitHub repository, build a new Docker image, and deploy our application every time a new commit is pushed to the main branch.

✨ **Key Features**
- **Automated Builds:** Jenkins automatically builds the project when changes are pushed.
- **Containerized Deployment:** The application is deployed as a Docker container for consistency and scalability.
- **Continuous Integration:** New code is automatically integrated and prepared for deployment.
- **Step-by-Step Learning:** The process is designed to teach the fundamentals of CI/CD in a practical way.

🛠️ **Tech Stack** This project uses the following technologies:

- **Backend:** Python with Flask
- **Containerization:** Docker
- **Automation Server:** Jenkins
- **Version Control:** Git & GitHub
- **API Testing:** Postman

🚀 **Getting Started** To run this project, you will need Docker and Java (for the Jenkins agent) installed on your machine.

**Clone the repository:**

```bash
git clone https://github.com/joaopblume/docker-flask-api-with-jenkins.git
```
