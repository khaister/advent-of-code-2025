# Advent of Code 2025

This repository contains my solutions for Advent of Code 2025, implemented in Python.

Website: <https://adventofcode.com/2025>

## Requirements

- Python 3.14 or newer
- Development tools: `ruff` (see `pyproject.toml` dev dependencies)

## Run

You can run individual day solvers directly or via the included `Makefile` targets.

- Run using Python module execution:
  - `uv run python -m day_1.part_1_solver`
  - `uv run python -m day_1.part_2_solver`

- Run using `make` targets:
  - `make day-1-part-1-solver`
  - `make day-1-part-2-solver`

## Repo layout

- `main.py` — small entry example
- `day_<n>/` — each day's folder contains `part_1_solver.py`, `part_2_solver.py`, `input.txt`, and `sample_input.txt`

Example (day 1): `day_1/`

## Adding a new day

1. Create `day_<n>/` directory.
2. Add `part_1_solver.py`, `part_2_solver.py`, `input.txt`, and `sample_input.txt`.
3. Optionally add `Makefile` targets or update the existing `Makefile`.

## Formatting

Run the code formatter configured in the repo:

```shell
make format
```

## Notes

- This project uses `pyproject.toml` for project metadata and dev dependencies.
- No license is specified.

## License

This project — **Advent of Code 2025** — is licensed under the
**GNU General Public License v3.0**.

See the [LICENSE](LICENSE) file for details.
