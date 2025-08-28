         # optimization_goal = modeler.minimize(modeler.max(modeler.end_of(job_interval)
         #                                                  for job_interval in job_intervals.values()))
 
        # TODO tardiness
         jobs_by_id = {j.id_job: j for j in problem_instance.jobs}
         jobs_components_grouped = [[jobs_by_id[i[0]] for i in group]
                                    for _k, group in itertools.groupby(traverse_instance_graph(problem_instance, search="components topological generations", yield_state=True),