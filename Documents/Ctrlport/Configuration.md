# Installation
First, you need to install networkx and matplotlib
The installation is quit simple, just follow the instruction written on the website
```
sudo pip2 install matplotlib
sudo pip install networkx
```
However, when we installed the two modules, we may still seen the error about "make sure matplotlib and networkx have been installed"
Then we turn to the sourcecode for ctrl-perf-monitor
[Source Code](http://gnuradio.org/redmine/projects/gnuradio/repository/revisions/d7a2a2b65407a8f1bc2c05747088e96a1f1b8315/entry/gnuradio-runtime/python/gnuradio/ctrlport/gr-perf-monitorx)
We find that this command leads to the error
```
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg
```
The reason is that, in the new version of matplotlib, 
NavigationToolbar2QTAgg => NavigationToolbar2QT
So the solution is correspondently simple. 
We locate the sourcecode file on our system, change the import package name.
The sourcefile's path is something like
~/your own path/target/bin/gr-perf-monitorx
change the NavigationToolbar2QTAgg to NavigationToolbar2QT
you will not see the error again.


# Set the configuration
Do not try to modify this file 
/target/etc/gnuradio/conf.d/gnuradio-runtime.conf
Because there is another global configuration file which could override the setting you changed.
So, even you set

```
[PerfCounters]
on = True#False
export = True#False
clock = thread
#clock = monotonic
[ControlPort]
on = True#False
edges_list = True#False
```

You still may see 

>Configuration has not turned on all of the appropriate ControlPort features:
>    [ControlPort] on = True
>    [ControlPort] edges_list = False
>    [PerfCounters] on = True
>    [PerfCounters] export = False

Change this one(You may need to create one if it doesn't exist)
~/.gnuradio/config.conf
and paste the following code

```
[PerfCounters]
on = True
export = True
clock = thread
#clock = monotonic
[ControlPort]
on = True
edges_list = True
```

You are all set.
Remember, do not add " #" after the value of "True" 