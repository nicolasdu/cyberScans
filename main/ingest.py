import json

from main.cache.cache import scan_ids_cache
from main.model.results import IngestionResult
from main.tasks import create_task
from flask import Blueprint

ingest_blueprint = Blueprint("ingest", __name__)


# ingest API that creates new scan ids in asynchronous behaviour
@ingest_blueprint.route("/scan", methods=["POST"])
def ingestion():
    scan = create_task.delay()
    scan_ids_cache[scan.id] = scan
    return json.dumps(IngestionResult(scan.id).__dict__)
