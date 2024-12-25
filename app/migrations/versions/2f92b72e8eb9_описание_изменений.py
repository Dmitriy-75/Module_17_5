"""Описание изменений

Revision ID: 2f92b72e8eb9
Revises: 7ba078ee115d
Create Date: 2024-12-16 16:03:13.507920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f92b72e8eb9'
down_revision: Union[str, None] = '7ba078ee115d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
