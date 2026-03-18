from dep_keystone.models import Package


def parse_requirements_txt(content: str):
    packages = []

    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("-r ") or line.startswith("--requirement "):
            raise ValueError("Include directives are not supported in v0.1.0")

        if "@" in line and "://" in line:
            raise ValueError("Direct URL dependencies are not supported in v0.1.0")

        name = line
        version = None

        if "==" in line:
            name, version = line.split("==", 1)

        packages.append(
            Package(
                name=name.strip(),
                version=version.strip() if version else None,
                ecosystem="python",
            )
        )

    packages.sort(key=lambda p: (p.name, p.version or ""))

    return [
        {
            "name": p.name,
            "version": p.version,
            "ecosystem": p.ecosystem,
        }
        for p in packages
    ]
