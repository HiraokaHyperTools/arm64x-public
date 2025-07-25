from invoke import task

@task
def dep(c):
    c.run("rd /s /q build\\html", echo=True, warn=True)
    c.run("make html", echo=True)
    c.run("copy nul build\\html\\.nojekyll", echo=True)
    c.run("robocopy /mir build\\html ..\\docs", echo=True)
