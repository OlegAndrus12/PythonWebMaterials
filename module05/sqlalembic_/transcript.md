pip install alembic

alembic init alembic

sqlalchemy.url = sqlite:///mydatabase.db

alembic revision -m "initial"


def upgrade() -> None:
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("on_vacation", sa.Boolean, default=False),
    )


def downgrade() -> None:
    op.drop_table("employee")

alembic upgrade head

show in postgress

alembic revision -m "adding job title"

def upgrade() -> None:
    op.add_column(
        "employee",
        sa.Column("role", sa.String(64), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("employee")


alembic current
alembic history
alembic downgrade -1
alembic downgrade 2b1ae634e5f7
alembic downgrade base


# show automatic

from todolist.models import Base
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

alembic revision --autogenerate -m "admin"