def parse_requirements_txt(content: str):
    packages = []

    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        packages.append(line)

    return sorted(packages)
