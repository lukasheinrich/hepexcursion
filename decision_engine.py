import time
import excursion
def run_smart_loop(problem,n_init, n_iterations,nsuggest = 1):
    overall_start = time.time()
    learner = excursion.Learner(problem)
    learner.initialize(n_init = n_init)
    print('initialized')
    yield learner
    for i in range(n_iterations):
        print('getting suggestion')
        new = learner.suggest(batchsize = nsuggest)
        print('evaluating at {}'.format(new))
        learner.evaluate_and_tell(new)
        yield learner
    total_time = time.time() - overall_start
    print(total_time)