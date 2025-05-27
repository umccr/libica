YAML_FILE = "swagger/openapi_public.yaml"


def strip(pattern):
    with open(YAML_FILE, "r") as f:
        lines = f.readlines()

    total = 0
    mod_lines = []

    for i, line in enumerate(lines):
        if pattern in line:
            print("Found on line %s: %s" % (i + 1, line))
            if pattern2 in mod_lines[-1]:
                del mod_lines[-1]
            total += 1
            continue
        mod_lines.append(line)

    with open(YAML_FILE, "w") as f:
        f.writelines(mod_lines)

    print("Total found: %s" % total)


if __name__ == '__main__':
    """
    You don't return anything if HTTP 204! Blank object {} is not appropriate here as the respective backing model; SDK
    generation will throw exception on non-nullable properties. So definition-wise, we simply need not to say anything. 
    So sweep these definitions if found.
    
    See https://github.com/OpenAPITools/openapi-generator/issues/476
    """

    pattern2 = "content:"

    strip(pattern="application/vnd.illumina.v3+json: {}")
    strip(pattern="application/vnd.illumina.v4+json: {}")
