"""Миграция3

Revision ID: 60d1297cdce2
Revises: 2f92b72e8eb9
Create Date: 2024-12-16 18:11:10.416593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60d1297cdce2'
down_revision: Union[str, None] = '2f92b72e8eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
