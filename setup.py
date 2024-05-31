from setuptools import setup
import platform
import sys


def get_python_version_string():
    major = sys.version_info.major
    minor = sys.version_info.minor
    return f"{major}.{minor}"


def get_platname():
    return platform.system()


current = get_python_version_string()
next = current.split(".")
next = f"{next[0]}.{int(next[1])+1}"
setup(
    name="OpenImageIO",
    version="2.6.2",
    options={
        "bdist_wheel": {
            "root_is_pure": False,
            "plat_name": get_platname(),
            "py_limited_api": f"cp{''.join(current.split('.'))}",
            # "python_tag": get_python_version_string(),
        },
    },
    include_package_data=True,
    python_requires=f">={current}, <={next}",
    package_dir={"": f"dist/lib/python{current}/site-packages"},
)
