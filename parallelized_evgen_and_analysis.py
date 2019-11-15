from generate_events import evgen_single_point
import joblib
import numpy as np
import pyhf

#This is e.g. Sherpa on MPI or a grid evgen task with several jobs
def run_evgen_in_parallel(x,nevents,parallelize = 10):
    njobs = parallelize
    events_per_subjob = nevents/njobs
    #run subjobs
    r = joblib.Parallel(n_jobs=njobs)(
        joblib.delayed(evgen_single_point)(x,e) for e  in [events_per_subjob]*njobs
    )
    return r

#This is Rivet or SimpleAnalysis after merge / hadd
def merge_parallel_runs_and_analyze(r,nevents):
    eff  =  np.sum(r)/nevents
    xsec =  30
    lumi =  1
    nevents = xsec * lumi * eff
    m = pyhf.simplemodels.hepdata_like([nevents],[50],[1])
    d = [50] + m.config.auxdata
    return np.log(pyhf.utils.hypotest(1.0,d,m))-np.log(0.05)    

#This is a single dataset task that is run in parallel and analyzed (Sherpa + Rivet + pyhf / Evgen + SimpleAnalysis + pyhf)
def run_single_point_mc(x,nevents = 10000, parallelize = 10):
    results        = run_evgen_in_parallel(x,nevents,parallelize=parallelize)
    analyze_result = merge_parallel_runs_and_analyze(results,nevents)
    return analyze_result

#This is more or less multiple dataset production jobs (could also be parallelizeds)
def run_multiple_points_mc(X,nevents = 10000, parallelize = 10):
    return np.asarray([run_single_point_mc(x,nevents,parallelize) for x in X])
