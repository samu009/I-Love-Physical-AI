def registra_robot(self ,robot_prodotti: list[Robot], robot: Robot)
    for(robot_prodotti in robot_prodotti[]){
        if (robot_prodotti.codice == self.robot.codice){ValueError}
    }
    robot_prodotti.append(self.robot)
    
def cerca_robot(self ,robot_prodotti: list[Robot],codice: str) -> Robot
    for(robot_prodotti in robot_prodotti[]){
        if (robot_prodotti.codice == self.codice){return robot_prodotti}
    }
    
def riepilogo_robot(self nome_azienda: str, robot_prodotti: list[Robot])->None
    for(robot_prodotti in robot_prodotti[]){
       print(robot_prodotti.modello ,robot_prodotti.stato ,robot_prodotti.peso_componenti)
    }
def __main__(self)
    self.robot = robot[]
    self.robot1 = robot("1243","mk1","magazzino",90.5,"pronto")
    self.robot1_1 = robot("1243","mk1","magazzino",93.5,"in collaudo")
    self.robot2 = robot("2143","mk2","applicazione",30.5,"in produzione")
    self.robot3 = robot("3421","mk3","magazzino",109.53,"pronto")
    self.robot4 = robot("4312","mk4","applicazione",19.4,"pronto")
    registra_robot(robot[],robot1)
    registra_robot(robot[],robot1_1)
    registra_robot(robot[],robot2)
    registra_robot(robot[],robot3)
    registra_robot(robot[],robot4)
    