def transform(legacy_data):
    return {m.lower(): n for n in legacy_data for m in legacy_data[n]}
