import math
from des import SchedulerDES
from event import Event, EventTypes
from process import ProcessStates


class FCFS(SchedulerDES):
        '''
        Implementation of FCFS/FIFO scheduling algorithms
        using OOP techniques
        '''

        def scheduler_func(self, cur_event):
                '''
                Parameters: Event object
                Returns: Process object with lease arrival time
                '''
                cur_proc_id = cur_event.process_id()
                cur_proc.run()
                return SchedulerDES.processes[cur_proc_id]

        def dispatcher_func(self, cur_proc):
                cur_proc.process_state(ProcessStates.RUNNING)
                return EventTypes.PROC_CPU_DONE


class SJF(SchedulerDES):
        def scheduler_func(self, cur_event):
                pass

        def dispatcher_func(self, cur_proc):
                pass


class RR(SchedulerDES):
        def scheduler_func(self, cur_event):
                pass

        def dispatcher_func(self, cur_proc):
                pass


class SRTF(SchedulerDES):
        def scheduler_func(self, cur_event):
                pass

        def dispatcher_func(self, cur_proc):
                pass
