# The __init__.py tells python to treat it as a package
# Import from a module
from my_module import my_func

my_func()

# Import from a package
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import some_sub_script

some_main_script.report_main()
some_sub_script.sub_report()