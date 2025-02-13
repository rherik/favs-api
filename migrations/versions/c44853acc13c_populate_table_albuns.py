"""populate table albuns

Revision ID: c44853acc13c
Revises: b8447c4ed4c8
Create Date: 2025-02-12 21:00:01.038128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer


# revision identifiers, used by Alembic.
revision = 'c44853acc13c'
down_revision = 'b8447c4ed4c8'
branch_labels = None
depends_on = None


def upgrade():
    accounts_table = table(
    "albuns",
    column("name", String),
    column("kind", String),
    column("creator", String),
    column("foto", String),
    column("release_date", String),
    column("description", String),
    column("rate", Integer)
    )
    op.bulk_insert(accounts_table, 
                   [{'name': 'Diamantes, Lágrimas e Rostos para Esquecer',
                     'kind': 'Rap',
                     'creator': 'BK',
                     'foto': 'none',
                     'release_date': '28/01/2025',
                     'description': 'Sexto album de estúdio do raper Abebe Bikila',
                     'rate': 4}])


def downgrade():
    pass
