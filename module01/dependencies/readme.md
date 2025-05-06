
# List of tools python uses for virtualenvs

0. nothing, everything is installed globally
1. virtualenv (third-party tool)
    1.1 Introduced in 2007.
    1.2 Created to solve the problem of dependency isolation across projects.
2. venv  (built in virtualenv)
    2.1 since python 3.3 (September 29, 2012)
    2.2 does not have a mechanism to solve conflicts
3. pipenv
    https://pipenv.pypa.io/en/latest/
    pip install --user pipenv
    has the lock file
    manages dependencies
    has venv
    pipenv --python 3.10
    pipenv --rm                         # Remove the current virtualenv
4. pyenv
    4.1 just the tool to manage python version
    4.2 pyenv install 3.12.2           # Install Python 3.12.2
    4.3 pyenv global 3.12.2            # Set it as global default
    4.4 pyenv local 3.10.8             # Set it for the current project dir
    4.5 pyenv versions                 # List installed versions
    4.6 pyenv uninstall 3.10.1         # Remove a version
    4.7 On Windows, pyenv is replaced by pyenv-win (a separate project).
    4.8 Not always necessary if you're only using one Python version.
    4.9 pyenv install --list
    4.10 pyenv global 3.12.2          # Set system-wide default version
    4.11 pyenv local 3.10.8           # Set version just for this directory/project
    4.12 pyenv shell 3.11.0           # Temporarily use a version in the current shell
    4.13 https://github.com/pyenv/pyenv
5. pipx
    https://pipx.pypa.io/stable/installation/
    pipx install pipenv
    pipx install poetry
6. poetry
    poetry add git+ssh://git@github.com/sdispater/pendulum.git


# pip

https://www.npmjs.com/package/left-pad
