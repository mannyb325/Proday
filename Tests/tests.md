# Using the `/test` Command: Good, Better, Best  

The `/test` slash command helps Copilot generate tests for your code. The more context and detail you provide, the better the generated tests. Here’s how you can apply “good, better, best” to `moving_average` in `test.py`:

---

## Good

> /test

**What happens:**  
Copilot attempts to generate a test, usually for the most recent or focused function (`moving_average`).  
- **Context:** Minimal; Copilot decides what to test and how.
- **Limitations:** May only create a basic test with default values, possibly missing important edge cases.

---

## Better

> /test Write tests for the `moving_average` function in `test.py`, covering normal and edge cases.

**What happens:**  
Copilot generates tests specifically for `moving_average`, likely including at least one “normal” case and some error cases.
- **Context:** Specifies the function and the file.
- **Clarity:** Requests edge case coverage.
- **Improvement:** More targeted and relevant tests.

---

## Best

> /test Write comprehensive pytest tests for the `moving_average` function in `test.py`, including:
> - Normal input (`[1, 2, 3, 4, 5, 6]`, window size 3, expect `[2.0, 3.0, 4.0, 5.0]`)
> - Edge case: window size equals data length
> - Edge case: window size 1 (should return original data)
> - Error: window size 0 (should raise ValueError)
> - Error: window size greater than data length (should raise ValueError)
> - Error: empty data list (should raise ValueError)
> Use clear, descriptive test function names and docstrings.

**What happens:**  
Copilot generates a robust suite of tests, covering all specified scenarios with clear names and documentation, using the `pytest` framework.
- **Context:** Complete (file, function, expected behaviors, framework).
- **Clarity:** Explicit about what to test and expected results.
- **Specificity:** Lists inputs, outputs, and error cases.

---
