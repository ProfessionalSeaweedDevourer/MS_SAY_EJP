"""Simple migration runner for local development.

Usage:
  python apply_migrations.py

This script loads `pivot_back/.env` (via python-dotenv) and executes SQL files
under `pivot_back/migrations/` against the SQLAlchemy `engine` exported by
`pivot_back/database.py`.

NOTE: Stop the backend server before applying migrations to avoid locked objects.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()

from pivot_back import database


def apply_sql_file(path: Path):
    sql = path.read_text(encoding='utf-8')
    # split by semicolon to allow multiple statements
    statements = [s.strip() for s in sql.split(';') if s.strip()]
    with database.engine.connect() as conn:
        with conn.begin():
            for stmt in statements:
                print('Executing:', stmt[:80].replace('\n',' '))
                conn.execute(text(stmt))


def main():
    repo_root = Path(__file__).resolve().parents[1]
    migrations_dir = repo_root / 'migrations'
    if not migrations_dir.exists():
        print('No migrations directory found:', migrations_dir)
        return

    for sql_file in sorted(migrations_dir.glob('*.sql')):
        print('Applying', sql_file.name)
        apply_sql_file(sql_file)

    print('Migrations applied.')


if __name__ == '__main__':
    main()
