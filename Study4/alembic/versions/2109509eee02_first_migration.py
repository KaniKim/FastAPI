"""First migration

Revision ID: 2109509eee02
Revises: 
Create Date: 2022-02-16 19:53:57.161149

"""
from email.policy import default
from xmlrpc.client import Boolean
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2109509eee02"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("email", sa.String(length=255), unique=True, index=True),
        sa.Column("hashed_password", sa.String(length=255)),
        sa.Column("is_active", sa, Boolean(), default=True),
    )
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("title", sa.String(), index=True),
        sa.Column("description", sa.String(), index=True),
        sa.Column("owner_id", sa.Integer(), sa.ForeignKey("users.id")),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("items")
