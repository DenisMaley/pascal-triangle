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
    triangle = Controller.get_pascal_triangle(number)
    for i in range(len(triangle)):
        print(triangle[i])


@cli.command()
@click.option(
    '--number', '-n',
    required=True,
    type=click.IntRange(1, None),
    default=1,
    help='Number of rows',
)
@click.option(
    '--divider', '-d',
    required=True,
    type=click.IntRange(2, None),
    default=2,
    help='Number of rows',
)
def sierpinski_triangle(number, divider):
    triangle = Controller.get_sierpinski_triangle(number, divider)
    for i in range(len(triangle)):
        row = ''
        for j in range(len(triangle[i])):
            row += ' ' if triangle[i][j] == 0 else '*'
        print(row)


if __name__ == '__main__':
    cli()
