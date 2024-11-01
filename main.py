from generator import Generator1
from argparse import ArgumentParser
import visual

parser = ArgumentParser()
parser.add_argument('-col',help='columnas',default=50)
parser.add_argument('-row',help='filas',default=50)
parser.add_argument('-x',help='columna inicial',default=0)
parser.add_argument('-y',help='fila inicial',default=0)

args = parser.parse_args()

rooms = int(args.row),int(args.col)
start_room = int(args.x),int(args.y)

generator = Generator1(rooms,start_room)
visual.init(generator.map.shape[0],generator.map.shape[1])
visual.run(generator)

input('ready')