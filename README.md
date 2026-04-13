# Research and Summarization Multi-Agent Workflow using LangGraph

This project is a **multi-agent AI workflow** built using **LangChain, LangGraph, and Google Gemini 2.5 Flash**.

It accepts a topic as input, performs factual research using one agent, and then simplifies the output using another agent. The main goal of this project is to demonstrate **state-based orchestration of LLM agents** in a structured and reusable workflow.

---

## Project Overview

This application is designed as a simple **Research-to-Summary AI pipeline**.

The workflow is managed using **LangGraph**, where each node represents a separate agent with a specific role.

### Workflow:
1. **Research Agent** collects factual information about the topic
2. **Summary Agent** converts the research into a simple explanation
3. The graph executes the flow from start to end

---

## Features

- Multi-agent workflow design
- State-based data passing using `TypedDict`
- Graph-based execution with LangGraph
- Factual research generation
- Beginner-friendly summarization
- Gemini 2.5 Flash integration
- Environment variable support using `.env`
- Basic error handling in agent functions

---

## Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini 2.5 Flash
- dotenv

---

## Project Structure

- **Research Agent**
  - Accepts user input
  - Generates factual bullet-point research output

- **Summary Agent**
  - Reads the research output
  - Explains the topic in simpler language
  - Adds a beginner-friendly teaching style

- **StateGraph**
  - Controls the workflow between agents
  - Passes state from one node to the next

---

## Code Concepts Used

This project demonstrates practical usage of:

- `ChatGoogleGenerativeAI`
- `SystemMessage` and `HumanMessage`
- `StateGraph`
- `TypedDict`
- prompt design for specialized agents
- sequential AI workflow execution

---

## Installation

```bash
pip install langchain langgraph langchain-google-genai python-dotenv
