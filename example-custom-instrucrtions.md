# Example: Copilot Repository Instructions (Illustration Only)

> ⚠️ **Note:**  
> This file is for demonstration purposes only.  
> GitHub Copilot will **not** read or use the instructions in this file, regardless of its name or location.

---

## Example Content for `.github/copilot-instructions.md`

Welcome!  
Below is an example of what you might put in a repository-level Copilot instructions file to guide contributors and illustrate best practices.  
**Again: Copilot will not enforce or use this file unless it is in the correct location and the feature is enabled.**

---

### Project Context

- This project contains both Python and Java code.
- Prioritize readability and maintainability.
- Code should be beginner-friendly and well-commented.

---

### Coding Preferences

- **Python:** Use type annotations, Google-style docstrings, and idiomatic code.
- **Java:** Use descriptive names, JavaDoc comments, and standard conventions.
- **Error Handling:** Always validate inputs and handle exceptions.
- **Testing:** Use pytest for Python, JUnit for Java.

---

### Copilot Suggestions

- When converting code between Python and Java, add comments explaining language differences.
- Prefer clear, explicit code over clever tricks.
- Include usage examples in `main` methods (Java) or `if __name__ == "__main__"` blocks (Python).
- For new files, provide a brief file-level comment or docstring.

---

## Example Section

**Python function:**
```python
def multiply(a: int, b: int) -> int:
    """Returns the product of a and b."""
    return a * b
```

**Java equivalent:**
```java
/**
 * Returns the product of a and b.
 */
public static int multiply(int a, int b) {
    return a * b;
}
```

---

## Why This is Good: The Four Pillars

- **Context:**  
  The instructions explain what kind of project this is (Python and Java), and highlight the importance of readability and maintainability, giving anyone (or any tool) a clear understanding of the project’s environment and priorities.

- **Intent:**  
  The file makes it explicit that the goal is to help contributors (and ideally Copilot, if supported) generate code that is beginner-friendly, well-documented, and consistent with project goals. It also states this is for illustration only.

- **Clarity:**  
  The instructions are direct and unambiguous, laying out exactly which conventions to follow for both Python and Java, how to handle errors, and how to write tests. The example code blocks demonstrate the expected style and formatting.

- **Specificity:**  
  Precise preferences are listed (docstring style, JavaDoc, error handling, test frameworks, where to put usage examples, etc.), removing guesswork and increasing the likelihood that contributors will match the desired code style.

---

*This file is for illustration only and does not affect Copilot's behavior.*
