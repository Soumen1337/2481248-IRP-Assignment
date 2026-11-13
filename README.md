# Placement Readiness Tracker

## Purpose
A Python command-line tool that records aptitude, verbal and coding practice
scores, calculates averages and grades, finds the top scorer, and flags
students whose average is below 40.

## Files
- `tracker.py` — main tracker (Tasks 1 and 2)
- `runnerup.py` — second-highest distinct score solution (Task 3)
- `screenshots/` — program-run and local Git-history evidence

## Requirements
Python 3.8 or later. No third-party packages are required.

## Run the tracker
```bash
python tracker.py
```
The application starts with five sample records and requests one additional
student. Enter a name, roll number and three whole-number scores from 0 to 100.
Invalid input is rejected and requested again.

## Run the runner-up solution
```bash
python runnerup.py
```
Input:
```text
5
70 85 85 60 90
```
Output:
```text
85
```

## Grade boundaries
| Average | Grade |
|---|---|
| 80 and above | A |
| 60 to below 80 | B |
| 40 to below 60 | C |
| Below 40 | Needs practice |

## Git workflow
The included local Git history has meaningful commits and a feature branch
merged into `main`. To publish the project, confirm that the supplied GitHub
repository exists, then connect and push:
```bash
git remote add origin https://github.com/Soumen1337/2481248-IRP-Assignment.git
git push -u origin main
```
A successful remote push is not represented by the local Git history.

## AI-use declaration
ChatGPT assisted with reviewing the assignment requirements, refining the
Python implementation, and preparing documentation. The author should review
and understand all submitted code and verify the outputs.

## Implementation notes
The tracker validates each entered score and uses the required function interfaces. The runner-up program uses distinct sorted scores.
