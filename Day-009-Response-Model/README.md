# Day 09 - FastAPI Response Model 🔐

> Learn how to control what your API returns to the client.

This is Day 09 of 100 Days of FastAPI.

### 🎯 What is Response Model?
In FastAPI, `response_model` is used to filter, validate and document your API output. It ensures you never accidentally leak sensitive data like passwords.

**Real-world example:** DB has `password` but client should only see `username, email`.

### 📂 Folder Structure