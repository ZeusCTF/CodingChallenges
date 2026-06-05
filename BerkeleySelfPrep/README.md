# Berkeley Self-Prep — C Systems Programming

Exercises covering core C systems programming topics. Each file contains a question prompt, my analysis, and the annotated code.

## Topics Covered

| File | Topic | Concept |
|------|-------|---------|
| `IO_question1.c` | File I/O | `fopen`, `getc`, newline counting |
| `IO_question2.c` | stdin reading | `fgets` vs `scanf` behavior |
| `concurrency_question1.c` | Processes | `fork`, interleaved output |
| `concurrency_question2.c` | Processes | Multiple `fork` calls, process tree |
| `flow_control_question1.c` | Loops | `for` loop variants, pre-decrement |
| `flow_control_question2.c` | Loops | `while` vs `do-while` |
| `functions_question1.c` | Functions / Arrays | Pass-by-pointer, in-place mutation |
| `operators_additional_question2.c` | Operators | Short-circuit evaluation, side effects |
| `operators_additional_question3.c` | Operators / Types | Unsigned integer underflow (infinite loop) |
| `operators_and_casting_question1.c` | Operators | Undefined behavior, lvalue constraints |
| `pointer_arithmetic.c` | Pointers | Manual `strcpy` implementation |
| `pointers_question1.c` | Pointers | Pointer traversal, memory addresses |
| `pointers_question2.c` | Pointers | `argv` traversal, nested pointer loops |
| `strings_question1.c` | Strings | `strtok`, dynamic memory |
| `strings_question2.c` | Strings | `sizeof` vs `strlen`, array decay |
| `strings_question3.c` | Strings | Mutable arrays vs string literals |
| `structures_question1.c` | Structs | Struct pointers, arrow operator |
| `structures_question2.c` | Structs | Struct padding / alignment |
| `system_calls_question1.c` | System Calls | `getenv`, `snprintf`, `system` |
| `system_calls_question2.c` | System Calls | `setenv`, `environ` |

## Key Takeaways

- `sizeof(array)` inside a function gives pointer size (8 bytes on 64-bit), not the array size — use `strlen` or pass the size explicitly
- Unsigned integers never go negative; `n-- >= 0` on an `unsigned` loops forever
- `fork()` duplicates the entire process; N sequential `fork()` calls create 2^N processes
- String literals are read-only; modifying them via a pointer causes a runtime segfault
- Struct members are padded for alignment; `sizeof(struct)` may exceed the sum of its members
