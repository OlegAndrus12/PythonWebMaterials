"""adding role

Revision ID: dff49f703335
Revises: 5f553576a06f
Create Date: 2025-05-22 17:54:44.403425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dff49f703335'
down_revision: Union[str, None] = '5f553576a06f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "employee",
        sa.Column("role", sa.String(64), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("employee")