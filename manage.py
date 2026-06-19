import os
import sys

# =====================================================================
# SYSTEM & DATABASE COMPATIBILITY PATCHES
# =====================================================================
try:
    import pymysql
    pymysql.version_info = (2, 2, 8, "final", 0)
    pymysql.install_as_MySQLdb()
    
    # 1. Nuke the version checks
    from django.db.backends.base.base import BaseDatabaseWrapper
    BaseDatabaseWrapper.check_database_version_supported = lambda self: None

    # 2. Force Django to stop appending "RETURNING" to SQL statements
    from django.db.backends.mysql.features import DatabaseFeatures
    DatabaseFeatures.can_return_rows_from_bulk_insert = False
    DatabaseFeatures.can_return_columns_from_insert = False
    DatabaseFeatures.has_select_for_update_skip_locked = False

except ImportError:
    pass
# =====================================================================


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empgt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()