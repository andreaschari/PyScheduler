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
                Returns: Process object with least arrival time
                '''
                cur_proc_id = cur_event.process_id()
                return SchedulerDES.processes[cur_proc_id]

        def dispatcher_func(self, cur_proc):
                cur_proc.process_state(ProcessStates.RUNNING)
                cur_proc.run_for(cur_proc.service_time(), self.time)
                cur_proc.process_state(ProcessStates.TERMINATED)
                return Event(process_id=cur_proc.process_id(), event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)


class SJF(SchedulerDES):
        def scheduler_func(self, cur_event):
                pass

        def dispatcher_func(self, cur_proc):
                pass


class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        for p in range(0, len(self.processes)):
            if self.processes[p].process_state() == ProcessStates.READY:
                return SchedulerDES.processes[p]

    def dispatcher_func(self, cur_proc):
        cur_proc.process_state(ProcessStates.RUNNING)
        cur_proc.run_for(SchedulerDES.quantum, self.time)
        if cur_proc.service_time() <= cur_proc.remaining_time():
            cur_proc.process_state(ProcessStates.READY)
            return Event(process_id=cur_proc.process_id(), event_type=EventTypes.PROC_CPU_REQ, event_time=self.time)
        else:
            cur_proc.process_state(ProcessStates.TERMINATED)
            return Event(process_id=cur_proc.process_id(), event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)


class SRTF(SchedulerDES):
        def scheduler_func(self, cur_event):
                pass

        def dispatcher_func(self, cur_proc):
                pass
