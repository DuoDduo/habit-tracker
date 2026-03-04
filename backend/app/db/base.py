"""
SQLAlchemy Base Configuration
Author: Blessing Oluwapelumi James
Matric No: 92134091
"""

# Import declarative_base function from SQLAlchemy ORM
# This function is used to create a base class for all ORM models
from sqlalchemy.orm import declarative_base

# Base class for all models
# declarative_base() generates a base class that:
#   • Maintains a catalog of mapped classes (ORM models)
#   • Provides metadata used for table creation
#   • Enables class-to-table mapping functionality
#
# All SQLAlchemy models in the project should inherit from this Base class.
# Example:
#   class Habit(Base):
#       __tablename__ = "habits"
#       ...
#
# This ensures:
#   • Consistent ORM behavior
#   • Automatic table registration
#   • Proper integration with SQLAlchemy's metadata system
Base = declarative_base()