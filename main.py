from decision_engine import run_smart_loop
import problems

def main():
    problem = getattr(problems,'simple_pyhf_problem')
    for learner in run_smart_loop(problem,3,7):
        print(learner.X)

if __name__ == '__main__':
    main()