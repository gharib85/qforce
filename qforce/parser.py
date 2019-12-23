import argparse
import os
import sys


def check_if_file_exists(file):
    if not os.path.exists(file) and not os.path.exists(f'{file}_qforce'):
        sys.exit(f'ERROR: "{file}" does not exist.\n')
    return file


def parse():
    depr = False
    options = ["init", "fragment", "fit"]
    opt_depr = ["dihedralfitting", "dipolefitting", "bondangle", "polarize",
                "input_traj", "input_dihedral"]
    opt_help = ('Optionally start the job at a specfic step:\n - '
                + '\n - '.join(options) + '\nOr use one of the depreciating' +
                ' options:\n - ' + '\n - '.join(opt_depr) + '\n\n\n')

    formatter = argparse.RawTextHelpFormatter
    parser = argparse.ArgumentParser(formatter_class=formatter)
    parser.add_argument('-f', type=check_if_file_exists, metavar='file',
                        help=('Input coordinate file (PBB, XYZ, GRO, ...)\n'
                              'or directory (job/job_qforce) name.'))
    parser.add_argument('-o', type=check_if_file_exists, metavar='options',
                        help='File name for the optional options.')
    parser.add_argument('-s', metavar='start', choices=options + opt_depr,
                        help=opt_help)
    parser.add_argument('-nofrag', default=False, action='store_true',
                        help='Skip flexible dihedrals')
    parser.add_argument('-p', metavar='params', nargs='+', type=float,
                        help='Set non-default empirical params (temporary)')
    args = parser.parse_args()
    if args.s in opt_depr:
        depr = True
    return args, depr
