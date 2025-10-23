# Reusable Prompt Examples for GitHub Copilot

Reusable prompts help you standardize quality across your team and streamline your workflow. You can copy and adapt these in Copilot Chat, PR comments, or documentation.

---

## 1. Add Type Annotations and Docstrings (Python)

> Add type annotations to all function parameters and return types in this file.  
> For each function, write a Google-style docstring explaining the arguments, return value, and any exceptions raised.

---

## 2. Generate Tests for a Function

> /test Write pytest tests for the `{function_name}` function, including:
> - A basic use case  
> - Relevant edge cases  
> - Cases where the function should raise exceptions  
> Use descriptive test function names and docstrings.

---

## 3. Refactor for Readability

> Refactor the following code to improve readability:
> - Use descriptive variable and function names  
> - Add comments where logic is complex  
> - Break large functions into smaller, single-purpose functions

---

## 4. Convert Between Languages

> Convert the `{function_name}` function from Python to Java.  
> Add comments explaining any major differences in types or behavior.  
> Write a JUnit test for the converted method.

---

## 5. Add Error Handling

> Review this function and add robust error handling.  
> Raise appropriate exceptions with clear messages for invalid input.

---

## 6. Document a Class

> Generate a comprehensive docstring for the `{ClassName}` class, including descriptions of all methods, parameters, and example usage.

---

## 7. Summarize Logic

> Summarize in plain English what the following function does, including an explanation of its algorithm and any edge cases it handles.

---

## How to Use

- Replace `{function_name}` or `{ClassName}` with your actual function or class.
- Paste the prompt in Copilot Chat or as a PR comment to get consistent, high-quality results.
- Customize for your team’s conventions as needed.

---
