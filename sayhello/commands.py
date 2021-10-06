import click

from sayhello import app, db
from sayhello.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''Initialize the database.'''
    if drop:
        click.confirm('将清空数据库，是否确定？', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('数据库初始化完成！')


