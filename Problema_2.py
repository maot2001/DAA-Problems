import random


class Problem_2:

    def __init__(self,N,M) -> None:
        """
        Argumentos:
        
        N: Cantidad de minutos
        M: Cantidad de eventos (debe ser menor que N)
        
        Propiedades:

        time: Tiempo (transcurre de 0.5 en 0.5 [1.0,1.5,...,N])

        events: Diccionario de eventos (Los eventos se encuentran en los tiempos t.5, por esta razon M debe ser menor que N)
        
        a: contador 1
        
        b: contador 2
        
        score: score calculado en la sol del usuario
        """
        #variables para trabajo externo
        self.time = self._list_create_(N)
        self.events = self._make_events_(M,N)
        self.a=0
        self.b=0
        self.score = 0

        self.__max_score__ = 0

    def _list_create_(self,N):
        time = []
        p = 1.0
        while p < N:
            time.append(p)
            p+= 0.5
        time.append(N)
        return time
    
    def _make_events_(self, M,N):
        events = {}
        count = 0
        while count != M:
            minutes = random.randint(1,N-1)
            T_i = minutes + 0.5
            C_i = random.randint(1,2)
            if T_i in events:
                continue
            events[T_i] = C_i
            count+=1
        return dict(sorted(events.items()))
    
    def _conditions_(self,C_i,a,b):
        if C_i == 1:
            if a > b:
                return True
            else:
                return False

        if C_i == 2:
            if a < b:
                return True
            else:
                return False
                
    def _brute_force_solution_(self, time,a=0,b=0,score=0):
        if len(time) == 1:
            self.__max_score__ = max(self.__max_score__,score)         
            return
        

        for i in range(len(time)):
            if i == len(time)-1:
                self.__max_score__ = max(self.__max_score__,score)         
                return


            minute = time[i]
            if minute in self.events:
                if (self._conditions_(self.events[minute],a,b)):
                    score+=1
                else:
                    a=0
                    b=0
            else:
                if minute % 1 == 0:
                    a+=1
                    self._brute_force_solution_(time[i+1:],a,b,score)
                    a-=1
                    b+=1
                    self._brute_force_solution_(time[i+1:],a,b,score)

    def evaluate_sol(self,user_score):
        if user_score == self.__max_score__:
            print("Resuelto")
        else:
            print("Todavia Falta")

    def solve(self):
        self._brute_force_solution_(self.time)


def Gen(number):
    problems = []
    for _ in number:
        N = random.randint(3,25)
        M = random.randint(2,N)
        p = Problem_2(N,M)
        problems.append(p)
    return problems


problems = Gen(10)


def Soluciones(problem : Problem_2):
    pass

    
