import json

from flask import Blueprint

from main.cache.cache import scan_ids_cache
from main.model.results import StatusResult
from main.tasks import app

status_blueprint = Blueprint("status", __name__)


@status_blueprint.route("/scan/<scan_id>", methods=["GET"])
def get_status(scan_id):
    if scan_ids_cache.get(scan_id, default='null') == 'null':
        return json.dumps(StatusResult(scan_id, "NOT-FOUND").__dict__)

    scan_result = app.AsyncResult(scan_id)
    if scan_result.status == 'PENDING':
        return json.dumps(
            StatusResult(scan_id,
                         "Accepted - the request for a new scan has been received and is pending processing").__dict__)
    elif scan_result.status == 'STARTED':
        return json.dumps(StatusResult(scan_id, "Running - the scan is currently running").__dict__)
    elif scan_result.status == 'SUCCESS':
        return json.dumps(StatusResult(scan_id, "Complete - the scan was completed successfully").__dict__)
    elif scan_result.status == 'FAILURE':
        return json.dumps(StatusResult(scan_id, "Error - an error occurred during the scan").__dict__)
