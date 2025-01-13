from basic_colors import print_warning, print_error, verbose_print, BRed, BGreen, BYellow, BBlue, BPurple, BCyan, NC, set_verbose, VERBOSE

def test_colors():
    print(f'{BRed}C{BGreen}o{BYellow}l{BBlue}o{BPurple}r{BCyan}s{NC} test!')

def test_print_functions():
    print_warning("This is a warning message.")
    print("Verbose:", VERBOSE)
    set_verbose(False)
    verbose_print("This is a non-verbose message.")
    set_verbose(True)
    verbose_print("This is a verbose message.")
    print_error("This is an error message.")

if __name__ == "__main__":
    test_colors()
    test_print_functions()
