![GitHub License](https://img.shields.io/github/license/computational-biology-tue/digital-twin-demo)
[![Static Badge](https://img.shields.io/badge/Powered_by-Pixi-%23facc15)](https://pixi.prefix.dev/latest/)
[![Static Badge](https://img.shields.io/badge/Built_with-Lit-%23334eff?logo=lit&logoColor=%23334eff&labelColor=white)](https://lit.dev/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Backend Tests](https://github.com/Computational-Biology-TUe/digital-twin-demo/actions/workflows/test.yml/badge.svg)](https://github.com/Computational-Biology-TUe/digital-twin-demo/actions/workflows/test.yml)

# Digital Twin Demo Application
This repository contains a demo application for the Digital Twin in Healthcare course. During the workshop, we'll be discussing the entire application and how it's structured. You will be able to use this application as a template or starting point for your own projects. 

## Getting started
Because there are quite a lot of files here, we'd like to help you navigate all of this. First of all, let's start with managing the dependencies. The main dependency manager for this project is [Pixi](https://pixi.prefix.dev/latest/). This is a very fast and lightweight dependency manager that is designed to work even in complicated multi-language and multi-environment projects. You can install Pixi by following the instructions on their website. Once you have installed Pixi, you can run the following command to install all dependencies for this project:

```bash
pixi install
```

Because the frontend is a Node.js application, you will also need to install the Node.js dependencies. We have prepared a specific pixi task so this is dead simple. You can do this by running the following command:

```bash
pixi run frontend-install
```

### Adding new Python dependencies
If you want to add a new dependency, you can do so by running the following command:
```bash
pixi add <dependency>
```
This will add the dependency to the `pixi.toml` file and install it. You can also specify the version of the dependency by adding `@<version>` to the end of the dependency name. For example, if you want to add the `requests` library version 2.25.1, you can run the following command:
```bash
pixi add requests@2.25.1
```

### For the frontend
For the frontend, we use Node.js and npm for package management. Pixi will have automatically installed these dependencies for you, and if you've run the `pixi run frontend-install` command, you should be good to go. If you want to add a new dependency, you can do so by running the following sets of commands:

**Option 1: using `npm` (recommended)**
1. Navigate to the frontend folder:
```bash
cd frontend
```

2. Install the dependency using npm:
```bash
npm install <dependency>
```

**Option 2: using Pixi**
1. Run the following command:
```bash
pixi run npm install <dependency> --prefix frontend
```

## Why so complicated?
The application is structured in a way that is similar to how real-world software is built. Instead of one big application, we have built the application as a collection of small "services" that each have their own responsibilities. In this way, you can develop different parts of the application independently, and you can also replace parts of the application with your own implementations.

### How to extend the application
Services contain various parts. This is how you can extend the application:

**Backend**:
1. Create a new service in the `backend/app/services` folder. This is a Python file that defines the functionality of your service.
2. Create models for your service in the `backend/app/models` folder. These models define what the data that goes in and out of your service looks like. In this way, we can validate the data that is sent to your service and ensure that it is correct.
3. Create a new router in the `backend/app/api` folder. In there, you define the endpoints that your service exposes. Endpoints are the URLs that other parts of the application can use to interact with your service. You can also define the input and output data for your endpoints, which will be validated against the models you created in step 2. There are different types of endpoints, which may be used for different purposes. For example, you can create a GET endpoint to retrieve data from your service, or a POST endpoint to send data to your service.

[OPTIONAL]
If you are making a service that the frontend interacts with, you will also need to tell the frontend how to interact with your service and how it should respond to the data it receives.

**Frontend**:
1. Define your service in the `frontend/src/services` folder. This is a TypeScript file that defines how the frontend interacts with your service. You can define functions that send requests to your service and handle the responses. This will look similar to how the backend service is defined, but it will be in TypeScript instead of Python.
2. In the frontend, insert the places where your service is used and define how the frontend responds to the interactions with your service. For example, you can create a new page in the `frontend/src/pages` folder that displays the data from your service, or you can create a new component in the `frontend/src/components` folder that allows the user to interact with your service. This part may vary depending on what your service does and how it is used in the application. You can also use existing components and pages to interact with your service, or you can create new ones if needed.

### This sounds like a lot of work, is it really necessary?
Yes, it is. In real-world applications, you will often work in teams where different people are responsible for different parts of the application. By structuring the application in this way, we can ensure that different parts of the application can be developed independently and that they can be replaced with new implementations without affecting the rest of the application. This is a common practice in software development. 

Additionally, because each part of the application is defined in its own service, we can easily test each part of the application independently. In this way, for example, we start with developing the backend service, we then test those services independently, and when they work, we can move them into the frontend. If we get an error then, we know it's related to the frontend.

### Speaking of testing, where are the tests?
The tests for the backend services are located in the `backend/tests` folder. Each service and its corresponding endpoints should have their own test files. We use the `pytest` framework for testing. 

## Automatic checking of code quality and style
We also have added support for `ruff`, a fast code linter that will check that the code adheres to the same style everywhere, and will check for vulnerabilities and possible bugs. You can invoke a check with:

```
pixi run ruff check
```

And you can ask it to automatically fix errors it finds with:

```
pixi run ruff check --fix
```

You can also use ruff as a formatter:
```
pixi run ruff format
```

For more info, check out the [ruff documentation](https://docs.astral.sh/ruff/).

## Seeing the application in action
To see the application in action, you can run the backend and frontend services. You can do this by running the following commands in separate terminal windows:

First, we start up the backend service:
```bash
pixi run backend
```

Then, in a separate terminal window, we start up the frontend service:
```bash
pixi run frontend
```

You can then open your web browser and navigate to `http://localhost:5173` to see the application in action. You can also use the API endpoints directly by navigating to `http://localhost:8000/docs` to see the automatically generated API documentation.

This may not be a very exciting application, but it should be a good starting point for your digital twin application.

## An important note about data storage
This application is stateless. This means that the application does not store any data between requests. In your application, you may want to have some way of storing data in a database. For example, you may want to keep track of patients over time, or you want to store the results of your calculations.

In a similar way that we have added the BMI service, you can add a new service that interacts with a database. You can use any type of database you want. I encourage you to explore different types of databases and see which one works best for your application. You can also use an ORM (Object-Relational Mapping) library to interact with your database in a more Pythonic way. Some popular ORMs for Python are SQLAlchemy and Tortoise ORM, but this is not a requirement.

### Sensitive data
If you are working with sensitive data, please DO NOT upload any of it to GitHub. GitHub is not a secure place to store sensitive data. If you need to store sensitive data, please use a secure database or storage service. You can also separate your sensitive data parts of the project from the application. Below is an example of a situation where this can be useful:

You want to train an AI model on sensitive data, and use this model to make predictions in your application. To prevent sensitive data from leaking into your application, you can train the model in a separate project that is not connected to your application. The code can be in a separate GitHub repository, and the data is stored in a secure database (and not in the GitHub repository). 

After training, you can then export the trained model weights into your application to build a prediction service, and use it in your application without exposing any sensitive data. For demonstration purposes, you can build a mock database in SQLite, which is stored as a file wihtin the Github repository, and use this to demonstrate how your application works. This way, you can show the functionality of your application without exposing any sensitive data.

## Information about the tools used in this project
There may be several new tools that you may not be faimiliar with. Below is a brief description of some tools that may be new to you, and how they are used in this project.

### FastAPI
The backend of this application is built using [FastAPI](https://fastapi.tiangolo.com/). FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

### Vite
The frontend of this application is built using [Vite](https://vitejs.dev/). Vite is just used for development purposes.

### Lit
The frontend of this application is built using [Lit](https://lit.dev/). Lit is a simple library for building fast, lightweight web components. It is built on top of the Web Components standard, which allows you to create reusable components that can be used in any web application.

### TypeScript
The frontend of this application is built using [TypeScript](https://www.typescriptlang.org/). TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale. It is a superset of JavaScript, which means that any valid JavaScript code is also valid TypeScript code. TypeScript adds optional static typing to JavaScript, which can help you catch errors early and improve the maintainability of your code. It is also used to define the data models for the frontend, which are used to validate the data that is sent to and received from the backend services. This is similar to how we use Pydantic models in the backend to validate the data that is sent to and received from the backend services. In this way, we can ensure that the data is correct and that the frontend and backend are in sync with each other.

### Uvicorn
The backend of this application is run using [Uvicorn](https://www.uvicorn.dev/). Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. It is designed to be easy to use and to provide a high-performance server for your FastAPI application. 
