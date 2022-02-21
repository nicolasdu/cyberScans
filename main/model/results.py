class StatusResult:
    def __init__(self, scan_id, status):
        self.scan_id = scan_id
        self.status = status


class IngestionResult:
    def __init__(self, scan_id):
        self.scan_id = scan_id
