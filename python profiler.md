# python profiler

``` python
import line_profiler
import atexit

profile = line_profiler.LineProfiler()

atexit.register(profile.print_stats)
```

Add @profile at the place where you want to measure the performance data.

``` python
measure_it = int(sys.argv[1])

@profile
def test():
```