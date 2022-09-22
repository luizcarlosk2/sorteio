from ast import arg
from multiprocessing.connection import wait
import sys
from time import sleep
from typing import List, Dict
from random import randint
from time import sleep as sleep2
from xmlrpc.client import boolean

#Global vars
start: int = 0
args_tags: List[str] = ["-c", "-n", "-w"]


def main() -> None:
    "Entrypoint of program"
    args: Dict[str, str] = read_args()
    print(f"O seu número é o {int(args['-c'])}.")
    print(f"O sorteio será entre os números {start} e {args['-n']}.")
    print(f"A probabilidade de sorteio é de {round(100*1/len(range(start,args['-n']+1)),2)}%.")
    if '-w' not in args.keys():
        args['-w'] = 0
    if args['-w'] > 0:
        print(f"O sorteio ocorrerá em {args['-w']} segundos...")
        print(f"Aguarde...")
        sleep2(args['-w'])
    exec_drawn(args)
    exit(255)


def read_args() -> Dict[str, int]:
    """Read args from the prompt and check if it has the correct syntax

    Returns:
        Dict[str, int]: return the result of syntax, with the key as str and the value as int
    """
    
    # Messages
    message_args = 'Input error, please use the "-c -n -w (optional)" arguments.'
    message_int = 'Please, use int values in the arguments.'
    
    #
    args: List[str] = sys.argv[1:]
    args = [x_arg.lower() for x_arg in args]
    if len(args) % 2 != 0:
        print(message_args)
        exit(255)
    args: Dict[str, str] = list_to_dict(args)

    args_chaves: List(str) = list(args.keys())
    args_values: List(str) = list(args.values())
    
    # Check if any unknow value is present in the input args
    if any([True if x not in args_tags else False for x in args_chaves]):
        print(message_args)
        exit(255)

    # Check if all mandatiry args are inserted.
    if len(set(('-c', '-n')).intersection(set(args_chaves))) != 2:
        print(message_args)
        exit(255)
        
    # Change args values to int
    try:
        args_values: List(int) = [int(x) for x in args_values]
    
    except ValueError:
        print(message_int)
        exit(255)
    
    args: Dict[str, int] = dict(zip(args_chaves,args_values))
    return args


    
def list_to_dict(lista: List[str]) -> Dict[str, str]:
    """
    Return a dict from the list.
    """
    it = iter(lista)
    result = dict(zip(it, it))
    return result


def exec_drawn(args: Dict[str, int]) -> None:
    """
    Execute the drawn
    """    
    chosen: int = args['-c']
    drawn: int = randint(0,args['-n'])

    if drawn == chosen:
        print(f"Numero sorteado ({drawn}) confere com o seu!")
        print("ヽ(´▽`)/")
        print("\n")
        exit(0)
    else:
        print(f"O número sorteado foi o {drawn}")
        print("Tente novamente...")
        print("¯\(°_o)/¯")
        print("\n")
        exit(255)

if __name__ == "__main__":
    main()