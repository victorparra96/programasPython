class Tele:


    _TV = ['''
             ___________________
            |                    |
            |                    |
            |                    |
            |____________________|                 
                        ||
                    __/  \__ ''',   
         '''
             ____________________
            |    ____            |
            |      |   \  /      |
            |      |    \/       |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          1         |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          2         |
            |____________________|                 
                        ||
                    __/  \__ ''', '''
             ____________________
            |                    |
            |        CHANEL      |
            |          3         |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          4         |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          5         |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          6         |
            |____________________|                 
                        ||
                    __/  \__ ''', ''' 
             ____________________
            |                    |
            |        CHANEL      |
            |          7         |
            |____________________|                 
                        ||
                    __/  \__ ''', 
            ]
    
    def __init__(self, _is_turned_on):
        self._is_turned_on = _is_turned_on
        self._change_= 0
    
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()


    
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()
    
    
    def change_chanel_up(self):
        if self._is_turned_on == False:
            self._display_image()
        else:
            if self._change_== 7:
                self._change_ = 0

            self._change_ = self._change_ + 1 
            self._display_image()

    def change_chanel_down(self):
        if self._is_turned_on == False:
            self._display_image()
        else:    
            self._change_=self._change_ - 1
            if self._change_ == 0:
                self._change_ = 7
            elif self._change_ == -1:
                self._change_ = 7
            self._display_image()        
    
    def _display_image(self):
        if self._is_turned_on == True:
            if self._change_ == 0:
                print(self._TV[1])
            else:
                print(self._TV[self._change_ + 1])
        elif self._is_turned_on == False:
            print(self._TV[0])
        
def run():
    tv= Tele(_is_turned_on = False)

    while True:
        command = str(input(''' 
                ¿Qué deseas hacer?
                [p] render
                [a] pagar
                [u] cambiar arriba
                [d] cambiar abajo
                [s] salir'''))
        if command == 'p':
            tv.turn_on()
        elif command == 'a':
            tv.turn_off()
        elif command == 'u':
            tv.change_chanel_up()
        elif command == 'd':
            tv.change_chanel_down()    
        else:
            break


if __name__ == "__main__":
    run()