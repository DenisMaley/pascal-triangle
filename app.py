import click

from src.controller import Controller


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--number', '-n',
    required=True,
    type=click.IntRange(1, None),
    default=3,
    help='Number of rows',
)
def pascal_triangle(number):
    triangle = Controller(number).get_triangle()
    for i in range(len(triangle)):
        print(triangle[i])


if __name__ == '__main__':
    cli()
