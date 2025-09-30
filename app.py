import streamlit as st
import json
import os

# Simple todo list app
st.title("🎯 My Self-Deploying Todo List")
st.write("This app automatically deploys when I update the code!")

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# Add new task
with st.form("add_task"):
    task = st.text_input("What do you need to do?")
    if st.form_submit_button("Add Task") and task:
        tasks = load_tasks()
        tasks.append({"id": len(tasks) + 1, "task": task, "done": False})
        save_tasks(tasks)
        st.success("Task added!")

# Show tasks
st.header("Your Tasks:")
tasks = load_tasks()
for t in tasks:
    st.checkbox(t["task"], value=t["done"], key=t["id"])

st.info("Try adding a task! This app updates automatically when I push code.")
