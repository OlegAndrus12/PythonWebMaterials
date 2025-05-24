"""Initial

Revision ID: 5f553576a06f
Revises: 
Create Date: 2025-05-22 17:44:52.546952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f553576a06f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("on_vacation", sa.Boolean, default=False),
    )


def downgrade() -> None:
    op.drop_table("employee")
