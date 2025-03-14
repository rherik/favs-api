"""populate albuns

Revision ID: 80496e435dea
Revises: b6807133993a
Create Date: 2025-03-13 14:44:43.303726

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

# revision identifiers, used by Alembic.
revision = '80496e435dea'
down_revision = 'b6807133993a'
branch_labels = None
depends_on = None


def upgrade():
    accounts_table = table(
    "albuns",
    column("name", String),
    column("kind", String),
    column("creator", String),
    column("foto", String),
    column("release_date", Date),
    column("description", String),
    column("rate", Integer)
    )
    op.bulk_insert(accounts_table, 
                   [{'name': 'O Líder em Movimento',
                     'kind': 'Rap',
                     'creator': 'BK',
                     'foto': 'https://imagens-favs-local.s3.sa-east-1.amazonaws.com/olideremmovimento-baner.jpeg',
                     'release_date': '2020-09-08',
                     'description': 'Este é o terceiro álbum de estúdio solo do artista da Pirâmide Perdida, BK. Mais introspectivo, não há participações especiais.',
                     'rate': 5}])


def downgrade():
    op.drop_table('albuns')
