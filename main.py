import click
import sys
from github import Github


@click.group('Update Tool')
def cli():
    pass


@cli.command()
@click.option('-l', '--repo-url', help='Github Repository Path {OWNER}/{REPO_NAME}')
@click.option('--ext', help='Select Custom Extension')
def github(repo_url, ext):
    if repo_url:
        update = Github(url=repo_url)
        update.ext = ext
        update.install()
        sys.exit(0)
    sys.stdout.write('Normal')


if __name__ == '__main__':
    cli()
