import os
import invoke

CONTAINER_NAME="phys434"

# changes working directory to root of project so tasks can be triggered from subdirs
cwd = os.getcwd()
while not os.path.isfile("./tasks.py") and cwd != "/":
    os.chdir(cwd + "/..")
    cwd = os.getcwd()


@invoke.task
def help(ctx):
    print(("Use inv -l to list tasks and inv -h <task> to see "
           "the help information about a specific task.  For help "
           "with invoke commands, use inv -h or `inv --help`"))


@invoke.task
def bup(ctx):
    """Runs docker build and docker-compose up -d"""
    ctx.run("docker build -t {}:latest . && docker-compose up -d".format(CONTAINER_NAME))


@invoke.task
def build(ctx):
    """executes 'docker build -t <container_name>:latest .'"""
    ctx.run("docker build -t {}:latest .".format(CONTAINER_NAME))


@invoke.task
def up(ctx):
    """executes 'docker-compose up -d'"""
    ctx.run("docker-compose up -d")


@invoke.task
def down(ctx):
    """executes 'docker-compose down'"""
    ctx.run("docker-compose down")
