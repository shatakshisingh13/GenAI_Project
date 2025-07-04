# ✅ Error Handling - Testing Report

This document outlines the tests conducted to ensure that the LinkedIn Post Generator gracefully handles various types of errors and edge cases during the metadata extraction and file processing stages.

---

## 🔍 Test Objectives

- Validate robustness of `extract_metadata()` and `get_unified_tags()` against invalid or partial responses.
- Ensure graceful handling of file decoding errors (e.g., corrupted or non-UTF-8 files).
- Simulate failure scenarios in the LLM pipeline.
- Confirm that unexpected outputs do not crash the system.

---

## 🧪 Test Cases

### 🧪 Test Case 1: Invalid JSON Response

**Description**: Simulate a scenario where the LLM returns a non-JSON response.

- **Input**: Plain string `"This is not a JSON!"`
- **Expected Result**: Should raise `OutputParserException`.

✅ **Pass**

---

### 🧪 Test Case 2: LLM Invocation Failure

**Description**: Simulate a failure in the LLM engine (e.g., timeout or crash).

- **Input**: Force an exception during `.invoke()`
- **Expected Result**: Should raise a standard `Exception`.

✅ **Pass**

---

### 🧪 Test Case 3: Corrupted Input File

**Description**: Attempt to load a file with invalid characters that don’t conform to UTF-8.

- **Input**: Binary file with invalid encoding bytes.
- **Expected Result**: Should not crash. File handled using `errors='ignore'`.

✅ **Pass**

---

### 🧪 Test Case 4: Incomplete Metadata JSON

**Description**: Simulate LLM returning only partial metadata (e.g., only `"line_count"` key).

- **Input**: JSON `{"line_count": 3}`
- **Expected Result**: Should raise `OutputParserException`.

✅ **Pass**

---

## ✅ Summary

| Test Case                    | Result  |
| ---------------------------- | ------- |
| Invalid JSON Response        | ✅ Pass |
| LLM Invocation Failure       | ✅ Pass |
| Corrupted File Handling      | ✅ Pass |
| Incomplete Metadata Response | ✅ Pass |

---

## 📌 Notes

- The tests were implemented using the built-in `unittest` module.
- `unittest.mock` was used to simulate LLM behaviors and failures.
- All test output files are cleaned up post-execution to avoid clutter.

---

## 🧪 To Run Tests

```bash
python test_error_handling.py
```
