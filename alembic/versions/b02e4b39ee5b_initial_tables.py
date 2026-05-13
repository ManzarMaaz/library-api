"""Initial tables

Revision ID: b02e4b39ee5b
Revises: 11559b0a6432
Create Date: 2026-04-23 13:06:50.372788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b02e4b39ee5b'
down_revision: Union[str, Sequence[str], None] = '11559b0a6432'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
