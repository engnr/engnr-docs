#!/usr/bin/env python3

import argparse
import subprocess
from termcolor import cprint


def main():
  parser = argparse.ArgumentParser(
    description='Documentation generation service.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-s', '--source', default='docs', help='Source directory')
  parser.add_argument('-o', '--output', default='build-docs', help='Output directory')
  parser.add_argument('-b', '--builder', default='html', help='Sphinx builder type')
  parser.add_argument('--once', action='store_true',
    help='Generate documentation once instead of doing so continuously')
  args = parser.parse_args()

  subprocess.run('sphinx-build -b {} {} {}'.format(args.builder, args.source, args.output), shell=True, check=True)
  if args.once:
    return

  print()
  result = subprocess.run('cd {} && nohup python3 -m http.server 80 &>/dev/null &'.format(args.output), shell=True)
  if result.returncode == 0:
      print('Server started successfully.')
  else:
      cprint('Failed to launch server. Open files in a browser manually as a fallback.', 'yellow')

  while True:
    print('\n====================================================================\n')
    result = subprocess.run('''\
      inotifywait -qq --recursive \
        --event modify --event move --event create --event delete \
        --exclude '/\..+' --exclude '/.+~' --exclude '/.+.sw?' \
        {}
      '''.format(args.source), shell=True)
    if result.returncode != 0:
      cprint('Unable to watch source folder.', 'red')
      break

    subprocess.run('sphinx-build -b {} {} {}'.format(args.builder, args.source, args.output), shell=True, check=True)


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print('\nQuitting')
