# Using the `/tests` Command: Good, Better, Best

The `/tests` slash command helps Copilot generate tests for your code. The more context and detail you provide, the better the generated tests. Here’s how you can apply “good, better, best” to Java test generation.

---

## Good

> /tests

**What happens:**  
Copilot attempts to generate a test, usually for the most recent or focused method (e.g., `movingAverage`).  
- **Context:** Minimal; Copilot decides what to test and how.
- **Limitations:** May only create a basic test with default values, possibly missing important edge cases.

---

## Better

> /tests Write tests for the `movingAverage` method, covering normal and edge cases.

**What happens:**  
Copilot generates tests specifically for `movingAverage`, likely including at least one “normal” case and some error cases.
- **Context:** Specifies the method.
- **Clarity:** Requests edge case coverage.
- **Improvement:** More targeted and relevant tests.

---

## Best

> /tests Write comprehensive JUnit tests for the `movingAverage` method, including:
> - Normal input (`[1, 2, 3, 4, 5, 6]`, window size 3, expect `[2.0, 3.0, 4.0, 5.0]`)
> - Edge case: window size equals data length
> - Edge case: window size 1 (should return original data as doubles)
> - Error: window size 0 (should throw IllegalArgumentException)
> - Error: window size greater than data length (should throw IllegalArgumentException)
> - Error: empty data list (should throw IllegalArgumentException)
> Use clear, descriptive test method names and JavaDoc comments.

**What happens:**  
Copilot generates a robust suite of tests, covering all specified scenarios with clear names and documentation, using the JUnit framework.
- **Context:** Complete (method, expected behaviors, framework).
- **Clarity:** Explicit about what to test and expected results.
- **Specificity:** Lists inputs, outputs, and error cases.

---
