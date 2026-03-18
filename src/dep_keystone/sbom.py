def build_sbom(normalized_graph: dict) -> dict:
    return {
        "bomFormat": "CycloneDX",
        "specVersion": "1.5",
        "version": 1,
        "metadata": {
            "tool": {
                "vendor": "Logos Governance Systems Inc.",
                "name": "DEP.KEYSTONE",
                "version": "0.1.0",
            }
        },
        "components": [
            {
                "type": "library",
                "name": pkg["name"],
                "version": pkg["version"],
                "properties": [
                    {"name": "ecosystem", "value": pkg["ecosystem"]}
                ],
            }
            for pkg in normalized_graph["packages"]
        ],
    }
