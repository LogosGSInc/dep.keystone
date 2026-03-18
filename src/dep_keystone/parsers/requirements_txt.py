def parse_requirements_txt(content: str):
    packages = []

    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        name = line
        version = None

        if "==" in line:
            name, version = line.split("==", 1)

        packages.append({
            "name": name.strip(),
            "version": version.strip() if version else None,
            "ecosystem": "python",
        })

    packages.sort(key=lambda p: (p["name"], p["version"] or ""))
    return packages
