""" Template for Project 1: Morse code """

from GPIOSimulator_v1 import *
import time
GPIO = GPIOSimulator()

MORSE_CODE = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
              '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
              '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
              '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
              '---..': '8', '----.': '9', '-----': '0'}

"...  .-  -.  -.-  .  -     -...  .  ....  .  .-.  .-"

#geeksforgeeks
#fidns the most frequent number in a list
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


class MorseDecoder():
    """ Morse code class """
    def __init__(self):
        """ initialize your class """
        GPIO.setup(PIN_BTN, GPIO.IN, GPIO.LOW)
        self.current_symbol = ""
        self.current_word = ""
        self.active_input = True
        self.T = 0.3


    def reset(self):
        """ reset the variable for a new run """
        self.current_symbol=""
        self.active_input=True

    def getsignalStatus(self):
        list_GPIOinput = []
        for i in range(100):
            list_GPIOinput.append(GPIO.input(PIN_BTN))
        #print(most_frequent(list_GPIOinput), "signal")
        return most_frequent(list_GPIOinput)


#reads one signal and returns ., -, endSymbol or endWord

    def read_one_signal(self):
        """ read a signal from Raspberry Pi """
        s = time.time()
        period = 0
        x = True
        if(self.getsignalStatus()==1):
           # print("h")
            while x:
                if(self.getsignalStatus() == 0):
                    period = time.time()-s
                    #print(period)
                    if (period <= 1.5*self.T):
                       # print(GPIO.input(PIN_BTN))
                        #print(".")
                        GPIO.output(PIN_BLUE_LED, GPIO.HIGH)
                        return "."
                    else:
                        #print("-")
                        GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
                        GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
                        GPIO.output(PIN_RED_LED_0, GPIO.HIGH)
                        return "-"
                    x = False

        if(self.getsignalStatus() == 0):
            while x:
                if (self.getsignalStatus() == 1):
                    period = (time.time()) - s
                    #print(period)
                    if (period < 1.5 * self.T):
                        return
                    elif (1.5*self.T < period <= 6.8 * self.T):
                             print("in")
                             return "endSymbol"

                    elif(period >= 7*self.T):
                        #print("ord endt")
                        return "endWord"


    def decoding_loop(self):
        """ the main decoding loop """
        self.process_signal(self.read_one_signal())


# delegates depending on what read_one_signal returns

    def process_signal(self, signal):
        """ handle the signals using corresponding functions """

        if(signal == "."):
            return self.update_current_symbol(".")
        elif(signal == "-"):
            self.update_current_symbol("-")
        else:
            if(signal == "endSymbol"):
                print("hhhhh")
                return self.handle_symbol_end()
            elif(signal == "endWord"):
                return self.handle_word_end()

    def update_current_symbol(self, signal):
        """ append the signal to current symbol code """
        self.current_symbol += signal
        print(self.current_symbol, "symbol oppdatert")


    def handle_symbol_end(self):
        """ process when a symbol ending appears """
        string = MORSE_CODE.get(self.current_symbol)
        if(string != None):
            self.current_word +=string
        self.current_symbol=""
        self.decoding_loop()


    def handle_word_end(self):
        """ process when a word ending appears """
        #self.current_word += MORSE_CODE[self.current_symbol]+" "
        string = MORSE_CODE.get(self.current_symbol)
        if(string != None):
            self.current_word +=string+" "
        self.show_message()
        self.reset()

    def handle_reset(self):
        """ process when a reset signal received """
        self.read_one_signal()

    def show_message(self):
        """ print the decoded message """
        print(self.current_word)


def main():
    """ the main function """
    mr = MorseDecoder()
    while True:
        mr.decoding_loop()


if __name__ == "__main__":
    main()

