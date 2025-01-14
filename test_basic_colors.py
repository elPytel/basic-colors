from basic_colors import *

def test_colors():
    print(f'{BRed}C{BGreen}o{BYellow}l{BBlue}o{BPurple}r{BCyan}s{NC} test!')
    print()

def test_print_functions():
    print_info("This is an info message.")
    print_warning("This is a warning message.")
    print_success("This is a success message.")
    print_error("This is an error message.", False)
    print()

def test_verbose_print():
    set_verbose(False)
    print_info("Verbose: " + Blue + str(is_verbose_on()) + NC)
    verbose_print("This is a non-verbose message.")
    set_verbose(True)
    print_info("Verbose: " + Blue + str(is_verbose_on()) + NC)
    verbose_print("This is a verbose message.", Purple)
    print()

if __name__ == "__main__":
    test_colors()
    enable_icons(True)
    test_print_functions()
    enable_icons(False)
    test_print_functions()
    test_verbose_print()
