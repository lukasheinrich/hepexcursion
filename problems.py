import excursion
from parallelized_evgen_and_analysis import run_multiple_points_mc 
simple_pyhf_problem = excursion.ExcursionProblem([
    run_multiple_points_mc
    ],
    thresholds = [0.0],
    ndim = 2,
    bounding_box = [[0,1],[0,1]]
)

