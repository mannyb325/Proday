# Good Prompt Example

## Prompt

> Convert this Python code to Java.

---

## What You Might Get from Copilot

Copilot may output a basic Java translation, but it might lack class structure, comments, exception handling, or demonstration code.

```java
public static List<Double> movingAverage(List<Double> data, int windowSize) {
    List<Double> averages = new ArrayList<>();
    for (int i = 0; i <= data.size() - windowSize; i++) {
        List<Double> window = data.subList(i, i + windowSize);
        double sum = 0;
        for (double num : window) {
            sum += num;
        }
        averages.add(sum / windowSize);
    }
    return averages;
}
```

---

## Notes

- Minimal guidance is provided to Copilot.
- The output may not follow Java best practices (e.g., missing class, missing `main` method, missing error handling).
- Not tailored for learning or clarity.
