from colorama import Fore, Style
from tabulate import tabulate
from html import entities
from sys import exit
from argparse import ArgumentParser

html_entities_dict = {char: '&'+code for code, char in entities.html5.items()}

parser = ArgumentParser(description="OKÉ: A tool to convert anything into anything.")
parser.add_argument("value", help="The value you need to encode (as a char by default).", nargs="+")
parser.add_argument("-c", "--char", help="The given input is a char.", action="store_true")
parser.add_argument("-d", "--dec", help="The given input is a decimal.", action="store_true")
parser.add_argument("-x", "--hex", help="The given input is a hex.", action="store_true")
parser.add_argument("-b", "--byte", help="The given input is a byte.", action="store_true")
args = parser.parse_args()


def f(val: str) -> str:
    return f"{Fore.BLUE}{val}{Style.RESET_ALL}"


def translate_char(value: str) -> None:
    translations = []
    translations.append([f("given"), value])
    translations.append([f("decimal"), f"{ord(value)}"])
    translations.append([f("hexadecimal"), "0x{:02x}".format(ord(value))])
    translations.append([f("byte"), "{:08b}".format(ord(value))])
    translations.append([f("URL"), "%{:02x}".format(ord(value))])
    translations.append([f("HTML name"), html_entities_dict[value] if value in html_entities_dict else "None"])
    translations.append([f("HTML dec"), "&#{:02x};".format(ord(value))])
    translations.append([f("HTML URL(dec)"), "%26%23{:02x};".format(ord(value))])
    translations.append([f("HTML hex"), "&#x{:02x};".format(ord(value))])
    translations.append([f("HTML URL(hex)"), "%26%23{:02x};".format(ord(value))])
    translations.append([f("Js unicode"), "\\u{:04x}".format(ord(value))])
    translations.append([f("URL 2ble"), "%25{:02x}".format(ord(value))])
    print(tabulate(translations, headers=[f("Format"), "Value"], tablefmt="pretty"))


def translate_dec(value: int) -> None:
    translations = []
    translations.append([f("decimal"), f"{value}"])
    translations.append([f("hexadecimal"), "0x{:02x}".format(value)])
    translations.append([f("byte"), "{:08b}".format(value)])
    print(tabulate(translations, headers=[f("Format"), "Value"], tablefmt="pretty"))


if __name__ == '__main__':
    for value in args.value:
        try:
            if args.char:
                if len(value) != 1:
                    print("[error] Give it char by char pls.")
                    exit(1)
                translate_char(value)

            elif args.dec:
                try:
                    translate_dec(int(value, 10))
                except ValueError:
                    print("[error] You didn't gave a valid decimal value.")
                    exit(1)

            elif args.hex:
                try:
                    translate_dec(int(value, 16))
                except ValueError:
                    print("[error] You didn't gave a valid hex value.")
                    exit(1)

            elif args.byte:
                try:
                    translate_dec(int(value, 2))
                except ValueError:
                    print("[error] You didn't gave a valid byte.")
                    exit(1)

            else:
                if len(value) != 1:
                    print("[error] This tool can handle only 1 char...")
                    exit(1)
                translate_char(value)
        except Exception as e:
            print("[error] An error occured please specify the right type for your input.")
            exit(1)

        if (args.value).index(value) != len(args.value)-1:
            print()
