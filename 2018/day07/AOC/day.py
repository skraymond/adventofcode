import pdb


class invalid_do(Exception):
    pass


class invalid_can_do(Exception):
    pass


class step_factory(object):
    def __init__(self):
        self.steps = {}

    def parse(self, line):
        step_name = line.split()[7]
        pre_name = line.split()[1]

        for name in (step_name, pre_name):
            if name not in self.steps:
                self.steps[name] = step(name)

        self.steps[step_name].add_preq(self.steps[pre_name])

    def parse_timed(self, line):
        step_name = line.split()[7]
        pre_name = line.split()[1]

        for name in (step_name, pre_name):
            if name not in self.steps:
                self.steps[name] = timed_step(name)

        self.steps[step_name].add_preq(self.steps[pre_name])

    def get_steps(self):
        return self.steps


class step(object):
    def __init__(self, name):
        self.name = name
        self.prereqs = []
        self._done = False

    def add_preq(self, pre):
        self.prereqs.append(pre)

    def do(self):
        if not self.can_do():
            raise invalid_do
        self._done = True
    
    def can_do(self):
        if self._done:
            raise invalid_can_do
        for pre in self.prereqs:
            if not pre.isDone():
                return False
        return True

    def isDone(self):
        return self._done


class timed_step(step):
    def __init__(self, name):
        step.__init__(self, name)
        self._time = 61 + (ord(name) - ord('A'))

    def do(self):
        if not self.can_do():
            raise invalid_do
        if not self._done:
            self._time -= 1
        if self._time == 0:
            self._done = True


class answer(object):
    def __init__(self, filename, oneline=None, number_of_workers=5):
        if filename is not None:
            self.f = open(filename)
            self.data = self.f.readlines()
        else:
            self.data = oneline
        self.number_of_workers = number_of_workers
        self.workers = []
        self.seconds = 0

    def generate(self):
        factory = step_factory()
        for line in self.data:
            factory.parse(line)
        self.steps = factory.get_steps()

    def generate_timed(self):
        factory = step_factory()
        for line in self.data:
            factory.parse_timed(line)
        self.steps = factory.get_steps()

    def run_a_step(self):
        for key in range(ord('A'), ord('Z') + 1):
            step_key = chr(key)
            if step_key not in self.steps:
                continue
            if not self.steps[step_key].isDone() and \
               self.steps[step_key].can_do():
                self.steps[step_key].do()
                return step_key
        return None

    def load_up(self):
        for key in range(ord('A'), ord('Z') + 1):
            step_key = chr(key)
            if step_key not in self.steps:
                continue
            if not self.steps[step_key].isDone() and \
               self.steps[step_key].can_do() and \
               len(self.workers) < self.number_of_workers and \
               self.steps[step_key] not in self.workers:
                self.workers.append(self.steps[step_key])
    
    def second_pass(self):
        self.seconds += 1
        for worker in self.workers:
            worker.do()
        finished = ""
        for i in reversed(range(len(self.workers))):
            if self.workers[i].isDone():
                finished += self.workers[i].name
                del self.workers[i]
        return "".join(reversed(list(finished)))

    def execute(self):
        self.generate()
        return_value = ""
        while True:
            step_key = self.run_a_step()
            if step_key is None:
                # pdb.set_trace()
                return return_value
            return_value += step_key

    def execute_two(self):
        self.generate_timed()
        
        finished = ""
        self.load_up()
        while len(self.workers) > 0:
            finished += self.second_pass()
            self.load_up()

        return finished
            
            

