# engnr-docs
Engnr team live documentation suite.


**Note.** All scripts are intended to be executed from the root of this repo.


1. Build Docker image by running `./docs image`.

1. Create initial documentation set by running `./docs init`.

   This script will create `docs` folder one level above relative to your local clone of this
   repo. Such behaviour enables linking this repo as a Git submodule into several projects at
   the same time.

1. Once you have documentation set configured just run `./docs watch`.

   This script listens to filesystem change events and automatically generates its output into
   `build-docs` folder.

1. Now edit documentation sources using your favourite text editor.

   Use browser of your choice to access `localhost:4000`. Hint: there are various browser
   plugins which can reload page automatically for your further convenience.

1. Use `./docs build` to power up your CI system with documentation publishing
   to GitHub/GitLab pages, etc.

**Note.** Run `./docs` without any arguments or pass `--help` to see help message.
Each subcommand has its additional help message.
