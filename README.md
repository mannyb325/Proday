# Proday
A repo for proday

The repo is intended to showcase best practices for Prompt Engineering.

This repo includes a skeleton setup for creating custom instructions and reusable prompt files

## Contents

- Skeleton setup for creating custom instructions
- Reusable prompt files in `copilot-prompts/`
- A simple python function

## Purpose

This repository is designed to help users learn and apply best practices in Prompt Engineering for AI and Copilot workflows.

## Good, Better, Best: Prompting Copilot to Convert Python Code to Java

**Good Prompt**  
Convert this Python code to Java.

---

**Better Prompt**  
Convert this Python function that calculates the moving average of a list of numbers with a specified window size to Java. Ensure the logic and functionality remain the same.

---

**Best Prompt**  
Convert the following Python function, which calculates the moving average of a list of numbers with a specified window size, to Java.  
- Implement the function as a static method in a Java class.  
- Use Java collections (e.g., `List<Double>`) for input and output.  
- Handle edge cases, such as window size greater than the list length or less than 1, with appropriate error handling or exceptions.  
- Preserve the algorithm’s logic and efficiency.  
- Add comments in the Java code to explain any differences or assumptions made during conversion.