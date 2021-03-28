import sys
import os
import argparse


"""Leemos cadena de un fichero de log"""
def read_text(name):
    f = open(name)
    return f.read()


def show_logs_ips(file_ips):
    """ Imprime los logs de todas las direcciones IPS que se encuentran en un fichero de texto"""
    ips = list()
    label_ips = read_text(file_ips).split("\n")

    for i in label_ips:
        if i != "":
            ips.append(i[2:])

    for i in sorted(ips):
        os.system(f"grep -ar {i} data/www.secrepo.com/self.logs")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Visualiza todos los logs ordenados del directorio data/www.secrepo.com/self.logs de las direcciones IPs contenidas en un fichero")
    parser.add_argument("-f", "--file_ips", nargs=1, help="Nombre del fichero")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    # Send a message to try the configuration of Telegram
    if args.file_ips:
        show_logs_ips(args.file_ips[0])
