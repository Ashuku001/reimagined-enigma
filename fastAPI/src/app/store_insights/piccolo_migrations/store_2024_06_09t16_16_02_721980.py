from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2024-06-09T16:16:02:721980"
VERSION = "1.7.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    def run():
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
