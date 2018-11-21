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
        Schedules next process to be executed
        Returns: Process object with least arrival time
        '''
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_proc):
        '''
        Parameters: Process object
        Runs current process and prepares the next event
        Returns: Event object
        '''
        cur_proc.process_state = ProcessStates.RUNNING
        cur_proc.run_for(cur_proc.service_time, self.time + cur_proc.arrival_time)
        cur_proc.process_state = ProcessStates.TERMINATED
        return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time + cur_proc.arrival_time)


class SJF(SchedulerDES):
    '''
    Implementation of Shortest Job First scheduling algorithm
    using OOP techniques
    '''

    def scheduler_func(self, cur_event):
        '''
        Parameters: Event object
        Schedules next process to be run
        Returns: Process object
        '''
        cur_proc = None
        for p in self.processes:
            if (p.process_state == ProcessStates.READY and cur_proc is None):
                cur_proc = p
            elif (p.process_state == ProcessStates.READY) and (p.service_time < cur_proc.service_time):
                cur_proc = p
        return cur_proc

    def dispatcher_func(self, cur_proc):
        '''
        Parameters: Event object
        Runs current process and prepares the next event
        Returns: Event Object
        '''
        cur_proc.process_state = ProcessStates.RUNNING
        cur_proc.run_for(cur_proc.service_time, self.time + cur_proc.arrival_time)
        cur_proc.process_state = ProcessStates.TERMINATED
        return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time + cur_proc.arrival_time)


class RR(SchedulerDES):
    '''
    Implementation of Round Robin scheduling algorithm
    using OOP techniques
    '''

    def scheduler_func(self, cur_event):
        '''
        Parameters: Event object
        Schedules next process to be run
        Returns: Process object
        '''
        for p in range(0, len(self.processes)):
            if self.processes[p].process_state == ProcessStates.READY:
                return self.processes[p]

    def dispatcher_func(self, cur_proc):
        '''
        Parameters: Event object
        Runs current process and prepares the next event
        Returns: Event Object
        '''
        quantum = self.quantum
        cur_proc.process_state = ProcessStates.RUNNING
        if quantum <= cur_proc.remaining_time:
            cur_proc.run_for(quantum, self.time + cur_proc.arrival_time)
            cur_proc.process_state = ProcessStates.READY
            return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + cur_proc.arrival_time)
        else:
            cur_proc.run_for(cur_proc.remaining_time, self.time + cur_proc.arrival_time)
            cur_proc.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time + cur_proc.arrival_time)


class SRTF(SchedulerDES):
    '''
    Implementation of Round Robin scheduling algorithm
    using OOP techniques
    '''

    def scheduler_func(self, cur_event):
        '''
        Parameters: Event object
        Schedules next process to be run
        Returns: Process object
        '''
        cur_proc = None
        for p in self.processes:
            if (p.process_state == ProcessStates.READY and cur_proc is None):
                cur_proc = p
            elif (p.process_state == ProcessStates.READY and p.remaining_time < cur_proc.remaining_time):
                cur_proc = p
        return cur_proc

    def dispatcher_func(self, cur_proc):
        '''
        Parameters: Event object
        Runs current process and prepares the next event
        Returns: Event Object
        '''
        quantum = 1 / self._arrivals_per_time_unit
        cur_proc.process_state = ProcessStates.RUNNING
        if quantum < cur_proc.remaining_time:
            cur_proc.run_for(quantum, self.time + cur_proc.arrival_time)
            cur_proc.process_state = ProcessStates.READY
            return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + cur_proc.arrival_time)
        else:
            cur_proc.run_for(cur_proc.remaining_time, self.time + cur_proc.arrival_time)
            cur_proc.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_proc.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time + cur_proc.arrival_time)
