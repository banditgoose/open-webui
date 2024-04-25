from peewee import *
from peewee_migrate import Router
from config import SRC_LOG_LEVELS, DATA_DIR, PG_HOST, PG_PORT, PG_USER, PG_DB, PG_PASS
import os
import logging

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["DB"])

# Check if the file exists
if os.path.exists(f"{DATA_DIR}/ollama.db"):
    # Rename the file
    os.rename(f"{DATA_DIR}/ollama.db", f"{DATA_DIR}/webui.db")
    log.info("File renamed successfully.")
else:
    pass


# TODO: set up a foolproof migration or rely on a new env variable to use postgres
DB = PostgresqlDatabase(user=PG_USER, password=PG_PASS,
                        host=PG_HOST, port=PG_PORT, database=PG_DB)
router = Router(DB, migrate_dir="apps/web/internal/migrations", logger=log)
router.run()
DB.connect(reuse_if_open=True)
