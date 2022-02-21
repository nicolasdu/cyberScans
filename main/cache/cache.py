from expiringdict import ExpiringDict

# cache in order to save the generated tasks
scan_ids_cache = ExpiringDict(max_len=20000, max_age_seconds=1200)
