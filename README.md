# Traffic Flow Analysis using Gaussian Elimination

## Overview
This project applies Gaussian Elimination from Linear Algebra to analyze traffic flow across multiple road intersections. The program models traffic intersections as a system of linear equations and computes the unknown traffic flow on each road.

## Features
- Dynamic number of intersections
- User-defined traffic flow inputs
- Automatic augmented matrix generation
- Gaussian Elimination implementation
- Back substitution for solving linear systems

## Technologies Used
- Python
- Linear Algebra
- Gaussian Elimination
- Matrix Operations
- Numerical Methods

## How to Run

```bash
python3 laa.py
```

## Sample Input

```
Enter number of intersections: 3
Intersection 1: 100
Intersection 2: 80
Intersection 3: 60
```

## Sample Output

```
Traffic flows on roads:
Road 1: 80
Road 2: 20
Road 3: 60
```

## Algorithm
1. Construct the augmented matrix.
2. Perform forward elimination.
3. Apply back substitution.
4. Display traffic flow for each road.

## Learning Outcomes
- Systems of Linear Equations
- Gaussian Elimination
- Matrix Manipulation
- Numerical Computing
