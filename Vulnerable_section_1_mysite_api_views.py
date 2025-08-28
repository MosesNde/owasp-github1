     enqueue_filter_job, enqueue_grayscale_job,
     wait_for_file, run_scipy_filter, run_scipy_gray,
     read_time, list_history, trim_history,
 )
 
 BASE_DIR = Path(__file__).resolve().parent
 
     def delete(self, _):
         # wipe all completed jobs
        for j in (BASE_DIR / "jobs").iterdir():
             if (j / "done.txt").exists():
                 from shutil import rmtree
                 rmtree(j, ignore_errors=True)
        return Response({"status": "cleared"}, status=204)