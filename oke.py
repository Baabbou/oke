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

parser.add_argument("-f", "--full-type", help="Convert a whole text and precise the type.")

args = parser.parse_args()


def blue(val: str) -> str:
    return f"{Fore.BLUE}{val}{Style.RESET_ALL}"


def translate_char(value: str) -> None:
    translations = []
    translations.append([0, blue("given"), value])
    translations.append([1, blue("decimal"), f"{ord(value)}"])
    translations.append([2, blue("hexadecimal"), "0x{:02x}".format(ord(value))])
    translations.append([3, blue("byte"), "{:08b}".format(ord(value))])
    translations.append([4, blue("URL"), "%{:02x}".format(ord(value))])
    translations.append([5, blue("HTML named"), html_entities_dict[value] if value in html_entities_dict else "None"])
    translations.append([6, blue("HTML num"), f"&#{ord(value)};"])
    translations.append([7, blue("HTML hex"), "&#x{:02x};".format(ord(value))])
    translations.append([8, blue("URL(HTML named)"), html_entities_dict[value].replace("&", "%26").replace(";", "%3b") if value in html_entities_dict else "None"])
    translations.append([9, blue("URL(HTML num)"), f"%26%23{ord(value)}%3b"])
    translations.append([10, blue("URL(HTML hex)"), "%26%23x{:02x}%3b".format(ord(value))])
    translations.append([11, blue("unicode"), "\\u{:04x}".format(ord(value))])
    translations.append([12, blue("URL2"), "%25{:02x}".format(ord(value))])
    print(tabulate(translations, headers=["Type", blue("Format"), "Value"], tablefmt="pretty"))


def translate_dec(value: int) -> None:
    translations = []
    translations.append([1, blue("ASCII"), chr(value)])
    translations.append([2, blue("decimal"), f"{value}"])
    translations.append([3, blue("hexadecimal"), "0x{:02x}".format(value)])
    translations.append([4, blue("byte"), "{:08b}".format(value)])
    print(tabulate(translations, headers=["Type", blue("Format"), "Value"], tablefmt="pretty"))


if __name__ == '__main__':

    if args.full_type:
        value = args.value[0]
        if args.full_type == "1":
            translation = " ".join([f"{ord(c)}" for c in value])

        elif args.full_type == "2":
            translation = " ".join(["0x{:02x}".format(ord(c)) for c in value])

        elif args.full_type == "3":
            translation = " ".join(["{:08b}".format(ord(c)) for c in value])

        elif args.full_type == "4":
            translation = "".join(["%{:02x}".format(ord(c)) for c in value])

        elif args.full_type == "5":
            translation = "".join([html_entities_dict[c] if c in html_entities_dict else "&#x{:02x};".format(ord(c)) for c in value])

        elif args.full_type == "6":
            translation = "".join([f"&#{ord(c)};" for c in value])

        elif args.full_type == "7":
            translation = "".join(["&#x{:02x};".format(ord(c)) for c in value])

        elif args.full_type == "8":
            translation = "".join([(html_entities_dict[c] if c in html_entities_dict else "&#x{:02x};".format(ord(c))).replace("&", "%26").replace("#", "%23").replace(";", "%3b") for c in value])

        elif args.full_type == "9":
            translation = "".join([f"%26%23{ord(c)}%3b" for c in value])

        elif args.full_type == "10":
            translation = "".join(["%26%23x{:02x}%3b".format(ord(c)) for c in value])

        elif args.full_type == "11":
            translation = "".join(["\\u{:04x}".format(ord(c)) for c in value])

        elif args.full_type == "12":
            translation = "".join(["%25{:02x}".format(ord(c)) for c in value])

        else:
            translation = "".join(["%{:02x}".format(ord(c)) for c in value])
        print(translation)

    else:
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
