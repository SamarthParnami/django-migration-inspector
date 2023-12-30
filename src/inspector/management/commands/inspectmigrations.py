from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser
from django.db.migrations.loader import MigrationLoader
from django.db.migrations.exceptions import CircularDependencyError, NodeNotFoundError, InconsistentMigrationHistory
from inspector.utils import InspectorConnectionHandler
from .constants import (DEFAULT_DB_ALIAS, CIRCULAR_DEPENDENCY_ERROR_MESSAGE, NODE_NOT_FOUND_ERROR_MESSAGE,
                    MULTIPLE_LEAF_NODE_ERROR_MESSAGE)

connections = InspectorConnectionHandler()

class Command(BaseCommand):
    help = "Checks the migrations for the list of all apps"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--database',
            default=DEFAULT_DB_ALIAS,
            help=f'Performs a migration order sanity check on the given database.Defaults to the "{DEFAULT_DB_ALIAS}" database.',
        )
        parser.add_argument(
            "--skip-history-check",
            action="store_true",
            help="Skip comparision with the already applied migrations.",
        )

    def handle(self, *args, **options):
        database = options['database']
        connection = connections[database]
        loader = self.prepare_loader()
        self._check_migration_files(loader)
        if not options["skip-history-check"]:
            self._check_migration_history(loader, connection)


    def prepare_loader(self):
        try:
            loader = MigrationLoader(None)
        except CircularDependencyError as e:
            self.stderr.write(CIRCULAR_DEPENDENCY_ERROR_MESSAGE.format(exception = str(e)))
            exit(1)
        except NodeNotFoundError as e:
            self.stderr.write(NODE_NOT_FOUND_ERROR_MESSAGE.format(exception = str(e)))
            exit(1)

        return loader

    def _check_migration_files(self, loader):
        conflicts = loader.detect_conflicts()
        if conflicts:
            seperator = '\n-'
            detail = "\n\n".join([f"[{app}]{seperator}{seperator.join(names)}"\
                                  for app, names in conflicts.items()])
            self.stderr.write(MULTIPLE_LEAF_NODE_ERROR_MESSAGE.format(detail = detail))
            exit(1)

    def _check_migration_history(self, loader, connection):
        try:
            loader.check_consistent_history(connection)
        except InconsistentMigrationHistory as e:
            self.stderr.write(str(e))
            exit(1)
