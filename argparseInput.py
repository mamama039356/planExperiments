import argparse

def commandline():
    parser = argparse.ArgumentParser(
        prog="tableArgparse",
        usage="Create table",
        description="good luck!",
        epilog="end",
        add_help=True
        )
    parser.add_argument("infile", help="inputfile")
    
    # 引数を解析する
    args = parser.parse_args()
    message = args.infile
    return message
    
if __name__ == "__main__":
    m = commandline()
    print(m)